from PySide6.QtWidgets import QWidget, QSizePolicy
from resources.ui.contacts_window_ui import Ui_contacts_window
from PySide6 import QtCore


class ContactsWindow(QWidget, Ui_contacts_window):

    go_to_previous_signal = QtCore.Signal()

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.pb_back.clicked.connect(self.go_to_previous_signal)
        self.lb_image.setMinimumSize(300, 300)
        self.lb_image.setMaximumSize(500, 500)
