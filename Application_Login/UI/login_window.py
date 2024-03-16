from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QIcon
from login_window_ui import Ui_Parent

class Login(QWidget, Ui_Parent):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.pb_log_in.clicked.connect(self.validate_login)
        self.le_user.textChanged.connect(self.hide_widget)
        self.le_password.textChanged.connect(self.hide_widget)
        self.switch_widget_state(self.lb_warning_icon, self.lb_warning_message, state_to_change=False)
        self.lb_warning_message.setVisible(True)
        
    def validate_login(self):
        if self.le_user.displayText() == "Jan" and self.le_password.text() == "Quality":
            print("continue")
        else:
            self.switch_widget_state(self.lb_warning_icon, self.lb_warning_message, state_to_change=True)

    def hide_widget(self):
        self.switch_widget_state(self.lb_warning_icon, self.lb_warning_message, state_to_change=False)
    
    def switch_widget_state(self, *widgets, state_to_change:bool):
        for widget in widgets:
            if widget.isVisible() is not state_to_change:
                widget.setVisible(state_to_change)
        