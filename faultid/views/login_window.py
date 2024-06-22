from PySide6.QtWidgets import QWidget
from PySide6 import QtCore
from resources.ui.login_window_ui import Ui_Parent

class LoginWindow(QWidget, Ui_Parent):
    # Define signals for various actions
    validate_login_signal = QtCore.Signal()
    go_to_info_signal = QtCore.Signal()
    go_to_add_serials_signal = QtCore.Signal()
    go_to_admin_signal = QtCore.Signal()
    go_to_manager_signal = QtCore.Signal()

    def __init__(self, app):
        """
        Initialize the LoginWindow.

        Args:
            app (QApplication): The Qt application instance.
        """
        super().__init__()
        self.setupUi(self)  # Set up the UI components
        self.app = app
        
        # Connect UI elements to corresponding signals
        self.pb_info.clicked.connect(self.go_to_info_signal)
        self.pb_log_in.clicked.connect(self.validate_login_signal)
        self.le_user.textChanged.connect(self.hide_credentials_error)
        self.le_password.textChanged.connect(self.hide_credentials_error)
        
        # Connect return (Enter) key to login validation
        self.le_user.returnPressed.connect(self.validate_login_signal)
        self.le_password.returnPressed.connect(self.validate_login_signal)
    
    def get_input_credentials(self):
        """
        Get the input credentials from the UI.

        Returns:
            dict: A dictionary containing 'email' and 'password' from the input fields.
        """
        return {'email': self.le_user.text(), 'password': self.le_password.text()}

    def hide_credentials_error(self):
        """
        Hide the credentials error message.
        """
        self.switch_widget_state(
            self.lb_warning_icon, self.lb_warning_message, state_to_change=False)

    def switch_error(self, state_to_change: bool):
        """
        Show or hide the credentials error message.

        Args:
            state_to_change (bool): The state to change the widgets to (True for show, False for hide).
        """
        self.switch_widget_state(
            self.lb_warning_icon, self.lb_warning_message, state_to_change=state_to_change)
    
    def switch_widget_state(self, *widgets, state_to_change: bool):
        """
        Change the state of specified widgets.

        Args:
            state_to_change (bool): The state to change the widgets to (True for enable, False for disable).
            *widgets: Variable length widget list to change state.
        """
        for widget in widgets:
            if widget.isEnabled() is not state_to_change:
                widget.setEnabled(state_to_change)
