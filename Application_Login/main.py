import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from UI.login_window_ui import Ui_Form


class LoginForm(qtw.QWidget, Ui_Form):

    login_success = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_Cancel.clicked.connect(self.close)

        self.pb_OK.clicked.connect(self.process_login)

    @qtc.Slot()
    def process_login(self):
        if self.le_UserID.text() == "Jan" and self.le_Password.text() == "Quality":
            self.login_success.emit()
            self.close()
        else:
            self.lb_Message.setText("You're not Jan!")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = LoginForm()
    window.show()

    sys.exit(app.exec())
