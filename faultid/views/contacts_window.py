from PySide6.QtWidgets import QWidget, QSizePolicy
from resources.ui.contacts_window_ui import Ui_contacts_window
from PySide6 import QtCore

class ContactsWindow(QWidget, Ui_contacts_window):
    """
    ContactsWindow class represents a QWidget displaying contacts information.
    """
    go_to_previous_signal = QtCore.Signal()

    def __init__(self, app):
        """
        Constructor for ContactsWindow.

        Args:
        - app: The application instance.
        """
        super().__init__()
        self.setupUi(self)  # Initialize the UI from the generated Ui_contacts_window class
        self.app = app  # Store the application instance

        # Connect signal to slot
        self.pb_back.clicked.connect(self.go_to_previous_signal)

        # Set minimum and maximum size for lb_image
        self.lb_image.setMinimumSize(300, 300)
        self.lb_image.setMaximumSize(500, 500)
