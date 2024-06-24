from concurrent.futures import ThreadPoolExecutor
import logging
from PySide6.QtWidgets import QMessageBox
import pandas as pd
from views.advanced_overview_window import AdvancedOverviewWindow

class AdvancedOverviewController:
    def __init__(self, app, model):
        self.model = model
        self.view = AdvancedOverviewWindow(app)
        self.parts = None
        self.view.radio_button_clicked_signal.connect(self.update_plots)
        self.view.export_data_signal.connect(self.export_data)
        self.raw_data_cache = {}
        self.processed_data_cache = {}
        self.invalidate_cache()  # Clear caches and initialize state
       
    def invalidate_cache(self):
        """Clear caches and reset state."""
        self.raw_data_cache.clear()
        self.processed_data_cache.clear()
        self.model.is_cache_invalid = False  # Reset cache validity flag
        logging.info("Cache invalidated.")
    
    def set_serials(self, serials):
        """Set the serial numbers to query."""
        self.model.set_serials(serials)

    def get_locations(self):
        """Retrieve available locations from the model."""
        return self.model.get_locations()

    def set_loading_message(self, loaded):
        """Update loading message based on loaded state."""
        if not loaded:
            self.view.lb_message.setText(
                "Loading... You will be able to see the data soon."
            )
        else:
            self.view.lb_message.setText(
                "Loaded. You can try again with another location."
            )
        self.view.sa_contents_buttons.setEnabled(loaded)

    def update_plots(self):
        """Update plots based on selected station."""
        self.view.pb_export.setEnabled(False)  # Disable export button
        selected_station = self.view.get_selected_location()
        self.set_loading_message(False)  # Show loading message

        try:
            # Retrieve data for input and other parts
            other_parts = self.get_other_parts(selected_station)
            input_parts = self.model.get_parameters(self.model.serials, selected_station)

            # Calculate outliers and cache processed data
            processed_data = self.calculate_outliers(input_parts, other_parts)
            self.processed_data_cache[selected_station] = processed_data
            self.plot_data(processed_data)  # Plot the processed data
            self.set_loading_message(True)  # Update message to loaded

        except ValueError as e:
            logging.error(f"ValueError: {e}")
            QMessageBox.critical(self.view, "Error", str(e))

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            QMessageBox.critical(self.view, "Error", f"An unexpected error occurred: {e}")

        finally:
            self.view.pb_export.setEnabled(True)  # Re-enable export button

    def get_other_parts(self, selected_station):
        """Retrieve other parts data using threading for asynchronous retrieval."""
        if self.model.is_cache_invalid:
            self.invalidate_cache()  # Reset caches if invalid

        if selected_station in self.raw_data_cache:
            return self.raw_data_cache[selected_station]

        # Use ThreadPoolExecutor to fetch other parts data asynchronously
        with ThreadPoolExecutor(max_workers=1) as executor:
            future_other_parts = executor.submit(
                self.model.get_params_for_scatter_plot,
                selected_station,
                self.set_loading_message,
            )
            other_parts = future_other_parts.result()  # Get the result from the future

        if other_parts is None:
            raise ValueError(
                "other_parts is None, not the result of the get_params_for_scatter_plot function"
            )

        self.raw_data_cache[selected_station] = other_parts  # Cache the retrieved data
        return other_parts

    def calculate_outliers(self, input_parts, other_parts):
        """Calculate outliers between input and other parts."""
        input_parts['created_at_numeric'] = input_parts['created_at'].apply(lambda x: x.timestamp())
        other_parts['created_at_numeric'] = other_parts['created_at'].apply(lambda x: x.timestamp())
        return self.model.calculate_outliers(input_parts, other_parts)

    def plot_data(self, data):
        """Plot data on the view."""
        self.view.clear_plots()  # Clear existing plots
        parameters = data["name"].unique()  # Get unique parameter names

        # Sort parameters by number of outliers
        parameters_sorted = sorted(parameters, key=lambda param: (
            (data[data["name"] == param]["part_type"] == "Other") & 
            (data[data["name"] == param]["is_outlier"] == True)).sum(), reverse=True)

        for parameter in parameters_sorted:
            data_param = data[data["name"] == parameter]
            input_parts_param = data_param[data_param['part_type'] == 'Input']
            other_parts_param = data_param[data_param['part_type'] == 'Other']
            blue_outliers = other_parts_param['is_outlier']
            parameter_limits = input_parts_param.iloc[0][["lower_limit", "upper_limit"]]

            # Create plot using view method
            self.view.create_plot(parameter, other_parts_param, input_parts_param, blue_outliers, parameter_limits)


    def export_data(self):
        """Export processed data to Excel."""
        export_location = self.view.get_export_path()  # Get export location from view
        if not export_location:
            return

        location = self.view.get_selected_location()  # Get selected location from view
        logging.info(f"Exporting data for location: {location} to {export_location}")

        try:
            export_successful = self.export_data_as_excel(self.processed_data_cache[location], export_location)
            if export_successful:
                self.view.lb_message.setText("Data exported successfully.")
            else:
                self.view.lb_message.setText("Data export failed.")

        except KeyError:
            logging.error("Selected location data not found in the cache.")
            QMessageBox.critical(self.view, "Error", "Selected location data not found in the cache.")

        except Exception as e:
            logging.error(f"Unexpected error during export: {e}")
            QMessageBox.critical(self.view, "Error", f"An unexpected error occurred during export: {e}")

    def export_data_as_excel(self, data, path):
        """Export data to Excel file."""
        try:
            with pd.ExcelWriter(path, engine='openpyxl') as writer:
                self.model.export_data_to_excel(writer, data, sheet_name='All_Data', table_name="Table_All_Data")
                parameters = data["name"].unique()

                for parameter in parameters:
                    red_outliers_data = data[(data["name"] == parameter) &
                                             (data["part_type"] == "Input") &
                                             (data["is_outlier"])]
                    blue_outliers_data = data[(data["name"] == parameter) &
                                              (data["part_type"] == "Other") &
                                              (data["is_outlier"])]
                    self.model.export_data_to_excel(writer, red_outliers_data, f'{parameter}_red_outliers', f"Table_{parameter.replace(' ', '_')}_red_outliers")
                    self.model.export_data_to_excel(writer, blue_outliers_data, f'{parameter}_blue_outliers', f"Table_{parameter.replace(' ', '_')}_blue_outliers")

            logging.info("Data export completed successfully.")
            return True

        except Exception as e:
            logging.error(f"Error exporting data to Excel: {e}")
            return False

    def get_other_parts_params(self):
        """Retrieve other parts parameters."""
        return self.model.get_other_parts(self.view.get_selected_location())

    def update_locations_filter(self):
        """Update radio buttons with available locations."""
        self.view.update_radio_buttons(self.get_locations())

    def pivot_table(self, parametrized_parts):
        """Pivot table for parametrized parts."""
        self.model.pivot_table(parametrized_parts)  # Delegate to model method
