from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QTableWidgetItem
from PySide6 import QtCore
from PySide6.QtGui import QColor

from resources.ui.overview_window_ui import Ui_OverviewWidget


class OverviewWindow(QWidget, Ui_OverviewWidget):
    radio_button_clicked_signal = QtCore.Signal()
    go_to_advanced_overview_signal = QtCore.Signal()

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.vb_locations = QVBoxLayout()
        self.vb_locations.setSpacing(14)
        self.sa_contents_buttons.setLayout(self.vb_locations)
        self.sa_radio_buttons.setWidget(self.sa_contents_buttons)
        self.tw_params.setCornerButtonEnabled(False)
        self.pb_advanced_overview.clicked.connect(self.go_to_advanced_overview_signal)

    def get_selected_location(self):
        radio_button = self.sender()
        if isinstance(radio_button, QRadioButton):
            if radio_button.isChecked():
                return radio_button.text()

    def update_radio_buttons(self, locations):
        for loc in locations:
            radio_button = QRadioButton(loc)
            radio_button.clicked.connect(self.radio_button_clicked_signal)
            self.vb_locations.addWidget(radio_button)

    def update_table(self, params):
        # Update the table widget with the new data
        self.tw_params.setRowCount(params.shape[0])
        self.tw_params.setColumnCount(params.shape[1])

        self.tw_params.setHorizontalHeaderLabels(params.columns.astype(str).tolist())
        self.tw_params.setVerticalHeaderLabels(params.index.astype(str).tolist())

        self.tw_params.resizeColumnsToContents()
        self.tw_params.resizeRowsToContents()

        for i in range(params.shape[1]):
            for j in range(params.shape[0]):
                value = params.iat[j, i]
                if isinstance(value, float):
                    if value.is_integer():
                        # If the float is an integer, format it with one decimal place
                        value = format(value, ".1f")
                    else:
                        # If the float is not an integer, format it with 10 decimal places
                        value = format(value, ".10f").rstrip("0")
                        if value[-1] == ".":
                            value += "0"

                self.tw_params.setItem(j, i, QTableWidgetItem(str(value)))
