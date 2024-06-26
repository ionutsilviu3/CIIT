from views.login_window import LoginWindow

class LoginController:
    def __init__(self, app, model):
        """
        Initialize the LoginController.

        Args:
            app (QApplication): The Qt application instance.
            model (UserModel): The user model to interact with the user data.
        """
        self.model = model
        self.view = LoginWindow(app)
        
        # Connect the validate_login_signal from the view to the validate_login method
        self.view.validate_login_signal.connect(self.validate_login)

    def validate_login(self):
        """
        Validate the user's login credentials and navigate to the appropriate view based on their role.
        """
        # Retrieve input credentials from the view
        input_credentials = self.view.get_input_credentials()
        
        # Check if the provided credentials are valid
        user_is_valid, result = self.model.is_valid(input_credentials)
        
        if not user_is_valid:
            self.view.switch_error(True, result)
            return
        
        # Get the role of the current user
        user_role = self.model.get_role(self.model.current_user_id)
        user_role = user_role['name'][0]
        
        # Emit the appropriate signal based on the user's role
        if user_role == "Admin":
            self.view.go_to_admin_signal.emit()
        elif user_role == "Manager":
            self.view.go_to_manager_signal.emit()
        elif user_role == "Engineer":
            self.view.go_to_add_serials_signal.emit()
        elif user_role == "Unregistered":
            # If the user is unregistered, modify their role to Engineer and then navigate
            self.model.modify_user_role(self.model.current_user_id, "Engineer")
            self.view.go_to_add_serials_signal.emit()

