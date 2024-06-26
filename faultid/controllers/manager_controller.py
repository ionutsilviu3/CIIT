from controllers.admin_controller import AdminController
from views.manager_window import ManagerWindow

class ManagerController(AdminController):
    def __init__(self, app, model):
        """
        ManagerController constructor.
        
        Args:
        - app: The application instance.
        - model: The model instance responsible for data operations.
        """
        super().__init__(app, model)
        
        # Set up ManagerWindow as the view for this controller
        self.view = ManagerWindow(app)
        
        # Connect signals from ManagerWindow to methods in this controller
        self.view.validate_signal.connect(self.validate_input_email)
        self.view.delete_user_signal.connect(self.delete_user)
        self.view.user_selected_signal.connect(self.user_selected)

    def user_selected(self, email, role):
        """
        Override method to handle user selection in ManagerWindow.
        """
        # Additional actions specific to ManagerController
        self.view.enable_delete_button()
