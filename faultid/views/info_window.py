from PySide6.QtWidgets import QWidget
from resources.ui.info_window_ui import Ui_info_window
from PySide6 import QtCore

class InfoWindow(QWidget, Ui_info_window):
    """
    InfoWindow class represents a QWidget displaying information with multiple pages.
    """
    # Signals for navigation
    go_to_previous_signal = QtCore.Signal()
    go_to_contacts_signal = QtCore.Signal()
    
    def __init__(self, app):
        """
        Constructor for InfoWindow.

        Args:
        - app: The application instance.
        """
        super().__init__()
        self.setupUi(self)  # Initialize the UI from the generated Ui_info_window class
        self.app = app  # Store the application instance

        # Connect signals to slots
        self.pb_back.clicked.connect(self.go_to_previous_signal)
        self.pb_previous_page.clicked.connect(self.go_to_previous_page)
        self.pb_next_page.clicked.connect(self.go_to_next_page)
        self.pb_contacts.clicked.connect(self.go_to_contacts_signal)

    def go_to_previous_page(self):
        """
        Slot method to navigate to the previous page in the stacked widget.
        """
        current_index = self.sw_pages.currentIndex()
        if current_index > 0:
            self.sw_pages.setCurrentIndex(current_index - 1)

    def go_to_next_page(self):
        """
        Slot method to navigate to the next page in the stacked widget.
        """
        current_index = self.sw_pages.currentIndex()
        if current_index < self.sw_pages.count() - 1:
            self.sw_pages.setCurrentIndex(current_index + 1)
