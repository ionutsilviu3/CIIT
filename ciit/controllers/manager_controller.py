from controllers.admin_controller import AdminController
from views.manager_window import ManagerWindow

class ManagerController(AdminController):
    def __init__(self, app, model):
        self.model = model
        self.view = ManagerWindow(app)
        self.view.validate_signal.connect(self.validate_input_email)
        self.view.delete_user_signal.connect(self.delete_user)
        self.view.user_selected_signal.connect(self.user_selected)

    def user_selected(self, email, role):
        self.view.enable_delete_button()