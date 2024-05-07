from concurrent.futures import Future
from datetime import datetime, timedelta
import threading
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn
from models.serial_model import SerialModel


class PartModel:

    def __init__(self, client, query_master):
        self.serials = []
        self.parts = None
        self.parametrized_parts = {}
        self.locations = []
        self.timeframes = None
        self.client = client
        self.query_master = query_master
        self.thread_result = None
        self.timeframe_scatter_plot = 8

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

            # Calculating PASS/FAIL result
            # parametrized_part['Result'] = np.where((parametrized_part['DCRD_VALUE_NUM']
            #                                         >= parametrized_part['DCDDC_LSL']) & (parametrized_part['DCRD_VALUE_NUM']
            #                                                                               <= parametrized_part['DCDDC_USL']), "PASS", "FAIL")
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

    # # get the production date when the given serials were produced
    # # TODO make this dynamic and smarter
    # def get_parts_production_datetimes(self):
    #     if self.timeframes is None:
    #         parts_production_datetimes = []
    #         try:
    #             for serial in self.serials:
    #                 query = self.query_master.get_last_datetime(serial=serial)
    #                 datetime = self.client.execute_query(query)
    #                 parts_production_datetimes.append(datetime["pe_endtime"])
    #         except Exception as e:
    #             print(
    #                 f"ERROR: Something went wrong when trying to get the datetime of the production of the following serials : {self.serials}."
    #             )
    #             print(e)

    #         df = pd.DataFrame(parts_production_datetimes)[0]

    #         # Sort the datetimes before converting them to strings
    #         df = df.sort_values()

    #         # Convert the sorted datetimes to strings
    #         self.timeframes = df.dt.strftime("%d.%m.%Y %H:%M:%S")

    #     # Returning sorted datetimes
    #     return self.timeframes

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
                        timedelta(hours=self.timeframe_scatter_plot)
                    end = datetime_obj + \
                        timedelta(hours=self.timeframe_scatter_plot)
                    timeframes.append((start, end))
                else:
                    # If it's not the first part, check the difference with the last timeframe
                    _, last_end = timeframes[-1]
                    diff = datetime_obj - last_end
                    if diff <= timedelta(hours=self.timeframe_scatter_plot * 2):
                        # If the difference is less than or equal to 16 hours, extend the last timeframe
                        timeframes[-1] = (
                            timeframes[-1][0],
                            datetime_obj +
                            timedelta(hours=self.timeframe_scatter_plot * 2),
                        )
                    else:
                        # If the difference is more than 16 hours, start a new timeframe
                        start = datetime_obj - \
                            timedelta(hours=self.timeframe_scatter_plot)
                        end = datetime_obj + \
                            timedelta(hours=self.timeframe_scatter_plot)
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

    def scatter_plot(self, input_parts, other_parts, parameter):
        other_parts_param = other_parts[other_parts["name"] == parameter]
        input_parts_param = input_parts[input_parts["name"] == {parameter}]

        seaborn.set_theme(style="dark")

        ax = seaborn.scatterplot(
            x="dcrd_created",
            y="dcrd_value_num",
            data=other_parts_param,
            label="Parts Produced",
        )
        seaborn.scatterplot(
            data=input_parts_param,
            x="dcrd_created",
            y="dcrd_value_num",
            ax=ax,
            label="Input Parts",
            marker="D",
            color="red",
            s=100,
        )
        plt.xlabel("Time")
        plt.ylabel("Parameter Value")
        plt.title("Scatter Plot of f{parameter} Value Over Time")
        plt.show()
