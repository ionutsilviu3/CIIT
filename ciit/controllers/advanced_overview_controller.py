from concurrent.futures import Future, ThreadPoolExecutor
from models.part_model import PartModel
from views.advanced_overview_window import AdvancedOverviewWindow


class AdvancedOverviewController:
    def __init__(self, app, model):
        self.model = model
        self.view = AdvancedOverviewWindow(app)
        self.parts = None
        self.view.radio_button_clicked_signal.connect(self.update_plots)

    def set_serials(self, serials):
        self.model.set_serials(serials)

    # get the stations of the serials given as input
    def get_locations(self):
        return self.model.get_locations()

    # TODO implement loading level
    def set_loading_message(self, loaded):
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

        with ThreadPoolExecutor(max_workers=1) as executor:
            future_other_parts = executor.submit(
                self.model.get_params_for_scatter_plot,
                self.view.get_selected_location(),
                self.set_loading_message,
            )

            # Wait for the future to finish and get its result
            other_parts = future_other_parts.result()

        # Make sure other_parts is not None before passing it to update_plots
        if other_parts is None:
            raise ValueError(
                "other_parts is None, not the result of the get_params_for_scatter_plot function"
            )

        self.view.update_plots(
            self.model.get_parameters(
                self.model.serials, self.view.get_selected_location()
            ),
            other_parts,
        )

    def get_other_parts_params(self):
        return self.model.get_other_parts(self.view.get_selected_location())

    def update_locations_filter(self):
        self.view.update_radio_buttons(self.get_locations())

    def pivot_table(self, parametrized_parts):
        self.model.pivot_table(parametrized_parts)

    def run(self):
        self.view.show()
