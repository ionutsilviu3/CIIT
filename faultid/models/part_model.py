from datetime import timedelta
import threading
import numpy as np
import pandas as pd
from scipy.spatial.distance import mahalanobis
from openpyxl.worksheet.table import Table, TableStyleInfo


class PartModel:
    def __init__(self, client, query_master, observer_model):
        self.serials = []
        self.locations = []
        self.timeframes = None
        self.client = client
        self.query_master = query_master
        self.thread_result = None
        self.plot_timeframe = 8
        self.limit_threshold = 0.2
        self.outlier_sensitivity_levels_input = 2
        self.outlier_sensitivity_levels_other = 2
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
        """
        Updates the part model with new settings from the observer model.
        """
        sensitivity_levels_input = {
            "low": 1.5,
            "normal": 2,
            "high": 2.5,
        }
        sensitivity_levels_other = {
            "low": 2.25,
            "normal": 2,
            "high": 1.2,
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

    def setup_locations(self):
        """
        Retrieves and sets up the locations (stations) where the serials were produced.
        """
        try:
            serials = "','".join(self.serials)
            query = self.query_master.get_stations_query(serials)
            stations = self.client.execute_query(query)

            for loc in stations["name"]:
                self.locations.append(loc)
        except Exception as e:
            print(
                f"ERROR: Something went wrong when trying to get the stations for the following serials: {
                    serials}"
            )
            print(e)

    def get_parameters(self, serials, station):
        """
        Retrieves parameters for the given serials produced at the specified station.

        Args:
            serials (list): List of serial numbers.
            station (str): Station name.

        Returns:
            DataFrame: Parameters DataFrame.
        """
        try:
            formatted_serials = "','".join(serials)
            query = self.query_master.get_parameters_query(
                formatted_serials, station)
            parametrized_part = self.client.execute_query(query)
            return parametrized_part
        except Exception as e:
            print(
                f"ERROR: Something went wrong when trying to get the parameters for the following serials produced at the {
                    station} station: {serials}"
            )
            print(e)
            return None

    def pivot_table_for_matrix(self, parametrized_part):
        """
        Creates a pivot table for matrix visualization from the parameterized part data.

        Args:
            parametrized_part (DataFrame): DataFrame of parameters.

        Returns:
            DataFrame: Pivot table.
        """
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
        """
        Creates a pivot table for scatter plot visualization from the parameterized part data.

        Args:
            parametrized_part (DataFrame): DataFrame of parameters.

        Returns:
            DataFrame: Pivot table.
        """
        if not parametrized_part.empty:
            parametrized_part = parametrized_part[
                ["unit_serial_number", "name", "value", "created_at"]
            ]
        return parametrized_part

    def get_params_for_scatter_plot(self, station, callback):
        """
        Fetches parameters for scatter plot visualization in a separate thread.

        Args:
            station (str): Station name.
            callback (function): Callback function to update UI or status.

        Returns:
            DataFrame: Parameters DataFrame for scatter plot.
        """
        thread = threading.Thread(
            target=self._get_params_for_scatter_plot_thread,
            args=(station, callback),
        )
        thread.daemon = True
        thread.start()
        thread.join()
        return self.thread_result

    def _get_params_for_scatter_plot_thread(self, station, callback):
        """
        Thread target function for fetching parameters for scatter plot visualization.

        Args:
            station (str): Station name.
            callback (function): Callback function to update UI or status.
        """
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
                    self.timeframes[0]} - {self.timeframes[1]} timeframe for the {station} station."
            )
            print(e)
            self.thread_result = None
        finally:
            callback(True)

    def get_parts(self, station):
        """
        Retrieves parts produced at the specified station within the defined timeframes.

        Args:
            station (str): Station name.

        Returns:
            DataFrame: Parts DataFrame.
        """
        parts = pd.DataFrame()
        try:
            for timeframe in self.timeframes:
                query = self.query_master.get_parts_produced(
                    station, timeframe[0], timeframe[1]
                )
                result = self.client.execute_query(query)
                parts = pd.concat([parts, result], ignore_index=True)
            parts = parts[~parts['unit_serial_number'].isin(self.serials)]
        except Exception as e:
            print(
                f"ERROR: Something went wrong when trying to get the parts produced in the given timeframes for the {
                    station} station."
            )
            print(e)
        return parts

    def divide_dataframe(self, df, chunk_size=1000):
        """
        Divides a DataFrame into smaller chunks.

        Args:
            df (DataFrame): DataFrame to divide.
            chunk_size (int): Size of each chunk.

        Returns:
            list: List of DataFrame chunks.
        """
        num_chunks = len(df) // chunk_size + (1 if len(df) %
                                              chunk_size != 0 else 0)
        chunks = np.array_split(df, num_chunks)
        return chunks

    def get_parameters_of_other_parts(self, other_parts, station):
        """
        Retrieves parameters for other parts produced at the specified station.

        Args:
            other_parts (DataFrame): DataFrame of other parts.
            station (str): Station name.

        Returns:
            DataFrame: Parameters DataFrame for other parts.
        """
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
        """
        Retrieves production datetimes for the serials and defines timeframes around those dates.

        Returns:
            list: List of timeframes as tuples of start and end datetimes.
        """
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
                    f"ERROR: Something went wrong when trying to get the datetime of the production of the following serials: {
                        self.serials}."
                )
                print(e)

            parts_production_datetimes = pd.concat(parts_production_datetimes)
            parts_production_datetimes.sort_values(inplace=True)

            timeframes = []
            for datetime_obj in parts_production_datetimes:
                if not timeframes:
                    start = datetime_obj - timedelta(hours=self.plot_timeframe)
                    end = datetime_obj + timedelta(hours=self.plot_timeframe)
                    timeframes.append((start, end))
                else:
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
            self.timeframes = [
                (start.strftime("%Y-%m-%d %H:%M:%S"),
                 end.strftime("%Y-%m-%d %H:%M:%S"))
                for start, end in tf
            ]
        return self.timeframes

    def calculate_mahalanobis_distances(self, blue_points, red_outlier_points):
        """
        Calculate Mahalanobis distances between blue points and red outlier points.

        Args:
            blue_points (ndarray): Array of blue points, the other parts.
            red_outlier_points (ndarray): Array of red outlier points, the outlier input parts.

        Returns:
            ndarray: 2D array of distances.
        """
        if blue_points.size == 0 or red_outlier_points.size == 0:
            return np.array([]).reshape(0, 0)

        cov_matrix = np.cov(blue_points, rowvar=False)
        inv_cov_matrix = np.linalg.inv(cov_matrix)

        distances = np.array([
            mahalanobis(blue_point, red_outlier, inv_cov_matrix)
            for blue_point in blue_points
            for red_outlier in red_outlier_points
        ])
        return distances.reshape(len(blue_points), len(red_outlier_points))

    def calculate_outliers(self, input_parts, other_parts):
        """
        Calculate outliers in the input parts based on the other parts.

        Args:
            input_parts (DataFrame): DataFrame of input parts.
            other_parts (DataFrame): DataFrame of other parts.

        Returns:
            DataFrame: Combined DataFrame with outlier labels.
        """
        parameters = input_parts["name"].unique()
        all_data = []

        for parameter in parameters:
            other_parts_param = other_parts[other_parts["name"] == parameter].copy(
            )
            input_parts_param = input_parts[input_parts["name"] == parameter].copy(
            )

            if other_parts_param.empty or input_parts_param.empty:
                continue

            parameter_limits = input_parts_param.iloc[0][[
                "lower_limit", "upper_limit"]]
            other_parts_param = other_parts_param.assign(**parameter_limits)

            blue_points = other_parts_param[[
                'created_at_numeric', 'value']].to_numpy()

            blue_value_mean = other_parts_param['value'].mean()
            blue_value_std = other_parts_param['value'].std()

            # Detecting only upper outliers for input parts
            red_outliers = input_parts_param['value'] > blue_value_mean + \
                self.outlier_sensitivity_levels_input * blue_value_std
            red_outlier_points = input_parts_param[red_outliers][[
                'created_at_numeric', 'value']].to_numpy()

            if red_outlier_points.size > 0:
                # Detecting only upper outliers for other parts
                blue_outliers = other_parts_param['value'] > blue_value_mean + \
                    self.outlier_sensitivity_levels_other * blue_value_std

                distances = self.calculate_mahalanobis_distances(
                    blue_points, red_outlier_points)
                if distances.size > 0:
                    min_distances = distances.min(axis=1)
                    threshold_distance = np.percentile(min_distances, 9)
                    close_blue_points = min_distances < threshold_distance
                    other_parts_param.loc[close_blue_points, 'is_close'] = True
                else:
                    other_parts_param.loc[:, 'is_close'] = False
            else:
                blue_outliers = np.zeros(len(other_parts_param), dtype=bool)
                other_parts_param.loc[:, 'is_close'] = False

            input_parts_param.loc[:, 'part_type'] = 'Input'
            input_parts_param.loc[:, 'is_outlier'] = red_outliers
            other_parts_param.loc[:, 'part_type'] = 'Other'
            other_parts_param.loc[:, 'is_outlier'] = blue_outliers

            combined_data = pd.concat([input_parts_param, other_parts_param])
            all_data.append(combined_data)

        combined_all_data = pd.concat(all_data)
        return combined_all_data

    def export_data_to_excel(self, writer, data, sheet_name, table_name):
        """
        Exports data to an Excel file with a specified sheet name and table name.

        Args:
            writer (ExcelWriter): Excel writer object.
            data (DataFrame): Data to export.
            sheet_name (str): Sheet name.
            table_name (str): Table name.
        """
        if not data.empty:
            data.to_excel(writer, sheet_name=sheet_name, index=False)
            worksheet = writer.sheets[sheet_name]
            table = Table(displayName=table_name, ref=worksheet.dimensions)
            style = TableStyleInfo(name="TableStyleMedium9", showFirstColumn=False,
                                   showLastColumn=False, showRowStripes=True, showColumnStripes=True)
            table.tableStyleInfo = style
            worksheet.add_table(table)

            for column in worksheet.columns:
                column_letter = column[0].column_letter
                max_length = max(len(str(cell.value)) for cell in column)
                adjusted_width = (max_length + 2)
                worksheet.column_dimensions[column_letter].width = adjusted_width
