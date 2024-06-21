from models.serial_model import SerialModel
from views.add_serials_window import AddSerialWindow


class AddSerialsController:
    def __init__(self, app, model):
        self.model = model
        self.view = AddSerialWindow(app)
        self.view.validate_signal.connect(self.validate_serial_with_db)
        self.view.delete_serials_signal.connect(self.delete_serials)
        self.view.clear_list_signal.connect(self.clear_serials)
        self.view.import_signal.connect(self.import_serials)
    
    def validate_serial_with_db(self):
        serial = self.view.get_input_from_user()
        result = self.model.validate_serial(serial)
        if result is not None:
            self.view.handle_error_message(True, custom_message=result)
        else:
            self.model.add_serial(serial)
            self.view.add_serial(serial)
            
    def import_serials(self):
        serials = self.get_serials_from_excel()
        problem_serials = 0
        size_of_serials = len(serials)
        if size_of_serials <= 0:
            self.view.handle_error_message(
                True,
                custom_message=f"There aren't any serials in the imported file.",
            )
        elif (
            size_of_serials + len(self.model.get_serials())
            > self.model.get_serials_limit()
        ):
            self.view.handle_error_message(
                True,
                custom_message=f"The list supports MAX {self.model.get_serials_limit()} serials.",
            )
 
        else:
            for serial in serials:
                validation_probs = self.is_serial_valid(serial)
                if validation_probs is None:
                    self.add_serial(serial)
                else:
                    problem_serials += 1
            if problem_serials > 0:
                self.view.handle_error_message(
                    True,
                    custom_message=f"{problem_serials} serials invalid and not imported.",
                )
                
    def get_serials_from_excel(self):
        path = self.view.get_excel_file_path()
        serials = self.model.read_serials_from_excel(path)
        return serials
    
    def add_serial(self, serial):
        self.model.add_serial(serial)
        self.view.add_serial(serial)

    def validate_input_serial(self):
        serial = self.view.get_input_from_user()
        result = self.is_serial_valid(serial)
        if result is not None:
            self.view.handle_error_message(True, custom_message=result)
        else:
            self.add_serial(serial)
 
    def is_serial_valid(self, serial):
        result = self.model.validate_serial(serial)
        return result
 
    def get_serials(self):
        return self.model.get_serials()
 
    def delete_serials(self):
        serials_to_delete = self.view.delete_serials()
        self.model.delete_serials(serials_to_delete)
 
    def clear_serials(self):
        self.model.clear_serials()
        self.view.clear_list()
