from models.part_model import PartModel
from views.overview_window import OverviewWindow


class OverviewController:
    def __init__(self, app, model):
        self.model = model
        self.view = OverviewWindow(app)
        self.view.radio_button_clicked_signal.connect(self.update_table)

    def set_serials(self, serials):
        self.model.set_serials(serials)

    # get the stations of the serials given as input
    def get_locations(self):
        return self.model.get_locations()

    def update_table(self):
        self.view.update_table(self.get_parameters())

    def get_parameters(self):
        station = self.view.get_selected_location()
        params = self.model.get_parameters(self.model.serials, station)
        # print(params)
        return self.model.pivot_table_for_matrix(params)

    def update_locations_filter(self):
        self.model.setup_locations()
        self.view.update_radio_buttons(self.get_locations())
        print(self.model.get_parts_production_datetimes())

    def run(self):
        self.view.show()
