from PySide6.QtWidgets import QWidget
from PySide6 import QtCore
from resources.ui.login_window_ui import Ui_Parent


class LoginWindow(QWidget, Ui_Parent):
    validate_login_signal = QtCore.Signal()
    go_to_add_serials_signal = QtCore.Signal()
    go_to_admin_signal = QtCore.Signal()
    go_to_manager_signal = QtCore.Signal()
    
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.pb_log_in.clicked.connect(self.validate_login_signal)
        self.le_user.textChanged.connect(self.hide_credentials_error)
        self.le_password.textChanged.connect(self.hide_credentials_error)
        self.le_user.returnPressed.connect(self.validate_login_signal)
        self.le_password.returnPressed.connect(self.validate_login_signal)
    
    def get_input_credentials(self):
        return {'email':self.le_user.text(), 'password':self.le_password.text()}

    def hide_credentials_error(self):
        self.switch_widget_state(
            self.lb_warning_icon, self.lb_warning_message, state_to_change=False)

    def switch_error(self, state_to_change: bool):
        self.switch_widget_state(
            self.lb_warning_icon, self.lb_warning_message, state_to_change=state_to_change)
    
    def switch_widget_state(self, *widgets, state_to_change: bool):
        for widget in widgets:
            if widget.isEnabled() is not state_to_change:
                widget.setEnabled(state_to_change)
        
