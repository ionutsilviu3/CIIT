from PySide6.QtWidgets import QWidget
from resources.ui.info_window_ui import Ui_info_window
from PySide6 import QtCore


class InfoWindow(QWidget, Ui_info_window):

    go_to_previous_signal = QtCore.Signal()
    go_to_contacts_signal = QtCore.Signal()
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.pb_back.clicked.connect(self.go_to_previous_signal)
        
        self.pb_previous_page.clicked.connect(self.go_to_previous_page)
        self.pb_next_page.clicked.connect(self.go_to_next_page)
        self.pb_contacts.clicked.connect(self.go_to_contacts_signal)
    def go_to_previous_page(self):
        current_index = self.sw_pages.currentIndex()
        if current_index > 0:
            self.sw_pages.setCurrentIndex(current_index - 1)
        
    def go_to_next_page(self):
        current_index = self.sw_pages.currentIndex()
        if current_index < self.sw_pages.count() - 1:
            self.sw_pages.setCurrentIndex(current_index + 1)
