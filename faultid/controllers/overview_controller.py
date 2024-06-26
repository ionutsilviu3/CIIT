from models.part_model import PartModel
from views.overview_window import OverviewWindow


class OverviewController:
    def __init__(self, app, model):
        """
        Initialize the OverviewController with the given application and model.

        Args:
        - app: The application instance.
        - model: The model instance that provides data.
        """
        self.model = model  # Store the model instance
        self.view = OverviewWindow(app)  # Create the overview window view
        self.view.radio_button_clicked_signal.connect(self.update_table)  # Connect signal to update table view

    def set_serials(self, serials):
        """
        Set the serials in the model.

        Args:
        - serials: List of serials to set.
        """
        self.model.set_serials(serials)

    def get_locations(self):
        """
        Retrieve the stations (locations) associated with the serials.

        Returns:
        - List of stations.
        """
        return self.model.get_locations()

    def update_table(self):
        """
        Update the table view in the overview window with parameters and limit threshold.
        """
        # Get selected station from view
        station = self.view.get_selected_location()
        # Get parameters based on selected station and model's serials
        params = self.model.get_parameters(self.model.serials, station)
        # Generate pivot table for matrix representation of parameters
        table_data = self.model.pivot_table_for_matrix(params)
        # Update view's table with parameters and limit threshold
        self.view.update_table(table_data, self.model.get_limit_threshold())

    def update_locations_filter(self):
        """
        Update the radio buttons in the view with available locations (stations).
        """
        self.model.setup_locations()  # Set up locations in the model
        locations = self.get_locations()  # Get updated locations
        self.view.update_radio_buttons(locations)  # Update radio buttons in the view
        print(self.model.get_parts_production_datetimes())  # Print parts production datetimes (for debugging)
