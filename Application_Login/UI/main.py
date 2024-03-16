from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from login_window import Login

app = QApplication()

window = Login()
window.show()

app.exec()