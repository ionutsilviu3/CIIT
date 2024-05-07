from models.serial_model import SerialModel
from views.add_serials_window import AddSerialWindow


class AddSerialsController:
    def __init__(self, app, model):
        self.model = model
        self.view = AddSerialWindow(app)
        self.view.validate_signal.connect(self.validate_serial_with_db)
        self.view.delete_serials_signal.connect(self.delete_serials)
        self.view.clear_list_signal.connect(self.clear_serials)

    def validate_serial_with_db(self):
        serial = self.view.get_input_from_user()
        result = self.model.validate_serial(serial)
        if result is not None:
            self.view.handle_error_message(True, custom_message=result)
        else:
            self.model.add_serial(serial)
            self.view.add_serials()

    def get_serials(self):
        return self.model.get_serials()

    def delete_serials(self):
        serials_to_delete = self.view.delete_serials()
        self.model.delete_serials(serials_to_delete)

    def clear_serials(self):
        self.model.clear_serials()
        self.view.clear_list()

    def run(self):
        self.view.show()
