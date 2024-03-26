from models.login_model import LoginModel
from views.login_window import LoginWindow


class LoginController:
    def __init__(self):
        self.model = LoginModel()
        self.view = LoginWindow()
        self.view.validate_login_signal.connect(self.validate_login)

    def validate_login(self):
        input_credentials = self.view.get_input_credentials()
        if self.model.is_valid(input_credentials) == True:
            self.model.set_credentials(input_credentials)
            return True
        else:
            self.view.switch_error(True)
            return False

    def run(self):
        self.view.show()
