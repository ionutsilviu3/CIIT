from views.admin_window import AdminWindow

class AdminController:
    def __init__(self, app, model):
        """
        Initialize the AdminController.

        Parameters:
        - app: Application instance (e.g., Qt application)
        - model: Data model instance providing access to user data

        This method sets up the AdminWindow view and connects signals to their corresponding slots.
        """
        self.model = model
        self.view = AdminWindow(app)  # Create an instance of AdminWindow
        # Connect signals from AdminWindow to their respective slot methods
        self.view.validate_signal.connect(self.validate_input_email)
        self.view.delete_user_signal.connect(self.delete_user)
        self.view.user_selected_signal.connect(self.user_selected)
        self.view.modify_role_signal.connect(self.modify_user_role)

    def add_new_user(self, email):
        """
        Add a new user with the provided email.

        Parameters:
        - email: Email address of the new user

        This method calls the model to add a new user and updates the view to reflect the change.
        """
        self.model.add_new_user(email)
        self.view.add_new_user(email)

    def delete_user(self, email):
        """
        Delete a user based on their email.

        Parameters:
        - email: Email address of the user to be deleted

        This method retrieves the user ID from the model using the email,
        deletes the user from the model, and updates the view.
        """
        user_id = self.model.get_user_by_email(email)['id'][0]
        self.model.delete_user(int(user_id))
        self.view.delete_user(email)

    def modify_user_role(self, email, new_role):
        """
        Modify the role of a user identified by their email.

        Parameters:
        - email: Email address of the user whose role is to be modified
        - new_role: New role to assign to the user ("Engineer" or "Manager")

        This method retrieves the user ID from the model using the email,
        retrieves role IDs for "Engineer" and "Manager" from the model,
        modifies the user's role in the model, and updates the view.
        """
        user_id = self.model.get_user_by_email(email)['id'][0]
        engineer_role_id = self.model.get_role_id_by_name("Engineer")
        manager_role_id = self.model.get_role_id_by_name("Manager")
        if new_role == "Engineer":
            self.model.modify_user_role(int(user_id), engineer_role_id)
        elif new_role == "Manager":
            self.model.modify_user_role(int(user_id), manager_role_id)
        self.view.modify_user_role(email, new_role)

    def user_selected(self, email, role):
        """
        Handle selection of a user in the view.

        Parameters:
        - email: Email address of the selected user
        - role: Role of the selected user ("Unregistered", "Engineer", or "Manager")

        This method enables or disables UI elements in the view based on the selected user's role.
        """
        if role != "Unregistered":
            self.view.enable_modify_role_button(role)
        self.view.enable_delete_button()

    def validate_input_email(self):
        """
        Validate input email entered in the view.

        This method retrieves the input email from the view,
        validates it using the model, and either displays an error message or adds the user.
        """
        email = self.view.get_input()
        result = self.is_email_valid(email)
        if result is not None:
            self.view.handle_error_message(True, custom_message=result)
        else:
            self.add_new_user(email)

    def is_email_valid(self, email):
        """
        Validate an email using the model.

        Parameters:
        - email: Email address to validate

        Returns:
        - True if the email is valid, False otherwise

        This method calls the model to validate the email format.
        """
        result = self.model.validate_email(email)
        return result

    def show_users(self):
        """
        Retrieve and display users based on the current user's role.

        This method retrieves subordinate users from the model based on the current user's role,
        sets the users in the view, and updates the view's chart.
        """
        user_role = self.model.get_role(self.model.current_user_id)
        user_role = int(user_role['id'][0])
        users = self.model.get_subordinate_users(user_role)
        self.view.set_users(users)
        self.view.update_chart()
