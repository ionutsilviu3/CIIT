from concurrent.futures import Future
from datetime import datetime, timedelta
import threading
import numpy as np
import pandas as pd
from models.serial_model import SerialModel
from scipy.spatial.distance import mahalanobis
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
from openpyxl.utils import column_index_from_string

class PartModel:

    def __init__(self, client, query_master, observer_model):
        self.serials = []
        self.locations = []
        self.timeframes = None
        self.client = client
        self.query_master = query_master
        self.thread_result = None
        self.plot_timeframe = 8
        self.limit_threshold = 0.05
        self.outlier_sensitivity_levels_input = 1.5
        self.outlier_sensitivity_levels_other = 1.5
        self.observer_model = observer_model
        self.observer_model.attach(self)
        self.is_cache_invalid = False
 
    def get_limit_threshold(self):
        return self.limit_threshold
 
    def get_plot_timeframe(self):
        return self.plot_timeframe
 
    def get_outlier_sensitivity_levels_input(self):
        return self.outlier_sensitivity_levels_input
 
    def get_outlier_sensitivity_levels_other(self):
        return self.outlier_sensitivity_levels_other
 
    def update(self, model):
        sensitivity_levels_input = {
            "low": 1.75,
            "normal": 2,
            "high": 2.25,
        }
        sensitivity_levels_other = {
            "low": 1.75,
            "normal": 2,
            "high": 2.25,
        }
        self.outlier_sensitivity_levels_input = (
            sensitivity_levels_input[model.settings["input_priority"]]
        )
        self.outlier_sensitivity_levels_other = sensitivity_levels_other[
            model.settings["other_priority"]
        ]
        self.limit_threshold = (
            model.settings["limit_sensitivity"] / 100
            if model.settings["limit_sensitivity"] > 0
            else 0
        )
        self.plot_timeframe = model.settings["timeframe"]
        self.timeframes = None
        self.get_parts_production_datetimes()
        self.is_cache_invalid = True

    def set_serials(self, serials):
        self.serials = serials

    def get_locations(self):
        return self.locations

    # get the stations of the serials given as input
    def setup_locations(self):
        try:
            serials = "','".join(self.serials)
            query = self.query_master.get_stations_query(serials)
            stations = self.client.execute_query(query)

            for loc in stations["name"]:
                self.locations.append(loc)
        except Exception as e:
            stations = None
            print(
                f"ERROR: Something went wrong when trying to get the stations in which the following serials were produced: {
                    serials}"
            )
            print(e)

    # get the parameters of the serials based on a station
    def get_parameters(self, serials, station):

        try:
            formated_serials = "','".join(serials)
            query = self.query_master.get_parameters_query(
                formated_serials, station)
            parametrized_part = self.client.execute_query(query)

            return parametrized_part
        except Exception as e:
            print(
                f"ERROR: Something went wrong when trying to get the parameters for the following serials produced in the {
                    station} station: {serials}"
            )
            print(e)
            return None

    def pivot_table_for_matrix(self, parametrized_part):
        if not parametrized_part.empty:
            parametrized_part = parametrized_part.drop_duplicates(
                subset=["name", "unit_serial_number"]
            )
            parametrized_part["name"] = (
                parametrized_part["name"]
                + "\n( "
                + parametrized_part["lower_limit"].map(str)
                + ", "
                + parametrized_part["upper_limit"].map(str)
                + " )"
            )
            parametrized_part = parametrized_part.pivot_table(
                index="name",
                columns=["unit_serial_number"],
                values=["value"],
                dropna=False,
            )
            parametrized_part.columns = parametrized_part.columns.get_level_values(
                1)

        return parametrized_part

    def pivot_table_for_scatter_plot(self, parametrized_part):
        if not parametrized_part.empty:
            parametrized_part = parametrized_part[
                ["unit_serial_number", "name", "value", "created_at"]
            ]

        return parametrized_part

    def get_params_for_scatter_plot(self, station, callback):
        # Create a new thread that will execute the long running query
        thread = threading.Thread(
            target=self._get_params_for_scatter_plot_thread,
            args=(station, callback),
        )
        thread.daemon = True
        thread.start()

        # Wait for the thread to finish
        thread.join()

        # Return the result directly
        return self.thread_result

    # TODO check why the callback doesn't update well
    def _get_params_for_scatter_plot_thread(self, station, callback):
        try:
            callback(False)
            params = self.get_parameters_of_other_parts(
                self.get_parts(station), station
            )
            params = self.pivot_table_for_scatter_plot(params)
            self.thread_result = params
        except Exception as e:
            print(
                f"ERROR: Something went wrong when trying to get the parts produced in the {
                    self.timeframes[0]} - {self.timeframes[1]} timeframe for a the {station} station."
            )
            print(e)
            self.thread_result = None
        finally:
            callback(True)

    def get_parts(self, station):
        parts = pd.DataFrame()
        try:
            for timeframe in self.timeframes:
                query = self.query_master.get_parts_produced(
                    station, timeframe[0], timeframe[1]
                )
                result = self.client.execute_query(query)
                parts = pd.concat(
                    [parts, result], ignore_index=True
                    # Use pd.concat() to concatenate the result DataFrame to parts
                )
            parts = parts[~parts['unit_serial_number'].isin(self.serials)]

        except Exception as e:
            print(
                f"ERROR: Something went wrong when trying to get the parts produced in the given timeframes for the {
                    station} station."
            )
            print(e)
        return parts

    # divide a dataframe in a given chunk size, mostly used for dynamic big queries
    def divide_dataframe(self, df, chunk_size=1000):
        # Get the number of chunks needed
        num_chunks = len(df) // chunk_size + (1 if len(df) %
                                              chunk_size != 0 else 0)

        # Use numpy.array_split() to split the DataFrame into chunks
        chunks = np.array_split(df, num_chunks)

        return chunks

    # get the parameters of all the other parts produced
    def get_parameters_of_other_parts(self, other_parts, station):
        if other_parts is None or other_parts.empty:
            return None
        parts_chunks = self.divide_dataframe(
            df=other_parts["unit_serial_number"], chunk_size=1000
        )

        parameters = pd.DataFrame()
        for chunk in parts_chunks:
            parameters = pd.concat(
                [parameters, self.get_parameters(
                    chunk.values.tolist(), station)]
            )
        return parameters.drop_duplicates()

    def get_parts_production_datetimes(self):
        if self.timeframes is None:
            tf = []
            parts_production_datetimes = []
            try:
                for serial in self.serials:
                    query = self.query_master.get_last_datetime(serial=serial)
                    datetime_obj = self.client.execute_query(query)["end_time"]
                    parts_production_datetimes.append(datetime_obj)
            except Exception as e:
                print(
                    f"ERROR: Something went wrong when trying to get the datetime of the production of the following serials : {
                        self.serials}."
                )
                print(e)

                # Concatenate the Series objects into a single Series
            parts_production_datetimes = pd.concat(parts_production_datetimes)

            # Sort the Series
            parts_production_datetimes.sort_values(inplace=True)

            timeframes = []
            for datetime_obj in parts_production_datetimes:
                if not timeframes:
                    # If it's the first part, start a new timeframe
                    start = datetime_obj - \
                        timedelta(hours=self.plot_timeframe)
                    end = datetime_obj + \
                        timedelta(hours=self.plot_timeframe)
                    timeframes.append((start, end))
                else:
                    # If it's not the first part, check the difference with the last timeframe
                    _, last_end = timeframes[-1]
                    diff = datetime_obj - last_end
                    if diff <= timedelta(hours=self.plot_timeframe * 2):
                        
                        timeframes[-1] = (
                            timeframes[-1][0],
                            datetime_obj +
                            timedelta(hours=self.plot_timeframe * 2),
                        )
                    else:
                        
                        start = datetime_obj - \
                            timedelta(hours=self.plot_timeframe)
                        end = datetime_obj + \
                            timedelta(hours=self.plot_timeframe)
                        timeframes.append((start, end))
            tf = timeframes
            # Convert the timeframes to strings
            self.timeframes = [
                (start.strftime("%Y-%m-%d %H:%M:%S"),
                end.strftime("%Y-%m-%d %H:%M:%S"))
                for start, end in tf
            ]

        # Returning timeframes
        return self.timeframes
    
    def calculate_mahalanobis_distances(self, blue_points, red_outlier_points):
        """Calculate Mahalanobis distances between blue points and red outlier points."""
        cov_matrix = np.cov(blue_points, rowvar=False)
        inv_cov_matrix = np.linalg.inv(cov_matrix)
        distances = np.array([mahalanobis(blue_point, red_outlier, inv_cov_matrix)
                            for blue_point in blue_points for red_outlier in red_outlier_points])
        return distances.reshape(len(blue_points), len(red_outlier_points))
    
    def export_data_to_excel(self, writer, data, sheet_name, table_name):
        if not data.empty:
            data.to_excel(writer, sheet_name=sheet_name, index=False)
            worksheet = writer.sheets[sheet_name]
            table = Table(displayName=table_name, ref=worksheet.dimensions)
            style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False, 
                                showLastColumn=False, showRowStripes=True, showColumnStripes=True)
            table.tableStyleInfo = style
            worksheet.add_table(table)
            
            # Autofit table columns
            dimensions = worksheet.calculate_dimension()
            for column in worksheet.columns:
                column_letter = column[0].column_letter
                max_length = max(len(str(cell.value)) for cell in column)
                adjusted_width = (max_length + 2)
                worksheet.column_dimensions[column_letter].width = adjusted_width
                
    def calculate_outliers(self, input_parts, other_parts):
        """
        Calculate outliers between input parts and other parts.

        Args:
            input_parts (pd.DataFrame): DataFrame containing input parts data.
            other_parts (pd.DataFrame): DataFrame containing other parts data.

        Returns:
            pd.DataFrame: Combined DataFrame with outliers information.
        """
        parameters = input_parts["name"].unique()
        all_data = []

        for parameter in parameters:
            # Filter parts for the current parameter
            other_parts_param = other_parts[other_parts["name"] == parameter].copy()
            input_parts_param = input_parts[input_parts["name"] == parameter].copy()

            if other_parts_param.empty or input_parts_param.empty:
                continue

            # Set limits for the current parameter
            parameter_limits = input_parts_param.iloc[0][["lower_limit", "upper_limit"]]
            other_parts_param.loc[:, "lower_limit"] = parameter_limits["lower_limit"]
            other_parts_param.loc[:, "upper_limit"] = parameter_limits["upper_limit"]

            # Calculate mean and standard deviation of the other parts
            blue_value_mean = other_parts_param['value'].mean()
            blue_value_std = other_parts_param['value'].std()

            # Identify outliers in the input parts
            red_outliers = (input_parts_param['value'] < blue_value_mean - self.outlier_sensitivity_levels_input * blue_value_std) | \
                        (input_parts_param['value'] > blue_value_mean + self.outlier_sensitivity_levels_input * blue_value_std)
            red_outlier_points = input_parts_param[red_outliers][['created_at_numeric', 'value']].to_numpy()

            # Identify outliers in the other parts
            if red_outlier_points.size > 0:
                blue_outliers = (other_parts_param['value'] < blue_value_mean - self.outlier_sensitivity_levels_other * blue_value_std) | \
                                (other_parts_param['value'] > blue_value_mean + self.outlier_sensitivity_levels_other * blue_value_std)
            else:
                blue_outliers = np.zeros(len(other_parts_param), dtype=bool)

            # Mark outliers and part types in the DataFrames
            input_parts_param.loc[:, 'part_type'] = 'Input'
            input_parts_param.loc[:, 'is_outlier'] = red_outliers
            other_parts_param.loc[:, 'part_type'] = 'Other'
            other_parts_param.loc[:, 'is_outlier'] = blue_outliers

            # Combine input and other parts data
            combined_data = pd.concat([input_parts_param, other_parts_param])
            all_data.append(combined_data)

        # Combine all data into a single DataFrame
        combined_all_data = pd.concat(all_data)
        return combined_all_data