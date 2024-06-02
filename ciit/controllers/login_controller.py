from views.login_window import LoginWindow


class LoginController:
    def __init__(self, app, model):
        self.model = model
        self.view = LoginWindow(app)
        self.view.validate_login_signal.connect(self.validate_login)

    def validate_login(self):
        input_credentials = self.view.get_input_credentials()
        user_is_valid = self.model.is_valid(input_credentials)
        if user_is_valid:
            user_role = self.model.get_role(self.model.current_user_id)
            user_role = user_role['name'][0]
            if user_role == "Admin":
                self.view.go_to_admin_signal.emit()
            elif user_role == "Manager":
                self.view.go_to_manager_signal.emit()  
            elif user_role == "Engineer":
                self.view.go_to_add_serials_signal.emit()
            elif user_role == "Unregistred":
                self.model.modify_user_role(self.model.current_user_id,"Engineer")
                self.view.go_to_add_serials_signal.emit()
        else:
            self.view.switch_error(True)
