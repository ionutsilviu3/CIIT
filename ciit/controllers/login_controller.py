from models.login_model import LoginModel
from views.login_window import LoginWindow


class LoginController:
    def __init__(self, app, model):
        self.model = model
        self.view = LoginWindow(app)
        self.view.validate_login_signal.connect(self.validate_login)

    def validate_login(self):
        input_credentials = self.view.get_input_credentials()
        if self.model.is_valid(input_credentials) == True:
            self.view.go_to_add_serials_signal.emit()
        else:
            self.view.switch_error(True)

    def run(self):
        self.view.show()
