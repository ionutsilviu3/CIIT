from PySide6.QtWidgets import QApplication
from controllers.login_controller import LoginController

app = QApplication()

login_controller = LoginController()
login_controller.run()

app.exec()