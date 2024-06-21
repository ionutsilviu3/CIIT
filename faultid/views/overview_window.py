import re
import math
from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QTableWidgetItem
from PySide6 import QtCore
from PySide6.QtGui import QColor

from resources.ui.overview_window_ui import Ui_OverviewWidget


class OverviewWindow(QWidget, Ui_OverviewWidget):
    radio_button_clicked_signal = QtCore.Signal()
    go_to_advanced_overview_signal = QtCore.Signal()
    go_to_settings_signal = QtCore.Signal()
    go_to_info_signal = QtCore.Signal()
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.vb_locations = QVBoxLayout()
        self.vb_locations.setSpacing(16)
        self.sa_contents_buttons.setLayout(self.vb_locations)
        self.sa_radio_buttons.setWidget(self.sa_contents_buttons)
        self.tw_params.setCornerButtonEnabled(False)
        self.pb_advanced_overview.clicked.connect(self.go_to_advanced_overview_signal)
        self.pb_settings.clicked.connect(self.go_to_settings_signal)
        self.pb_info.clicked.connect(self.go_to_info_signal)

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

    def parse_limits(self, row_name):
        """Extract the limits from the row name."""
        match = re.search(r'\(([^)]+)\)', row_name)
        if match:
            lower_limit, upper_limit = map(float, match.group(1).split(','))
            return lower_limit, upper_limit
        return None, None

    def is_close_to_limit(self, value, lower_limit, upper_limit, relative_sensitivity, absolute_sensitivity=0.1):
        value_float = float(value)

        # Calculate proximity threshold as a percentage of the range
        proximity_threshold_relative = relative_sensitivity * (upper_limit - lower_limit)
        
        # Combine with an absolute threshold to handle small ranges
        proximity_threshold = max(proximity_threshold_relative, absolute_sensitivity)
        
        # Check if the value is close to the limits
        return (lower_limit <= value_float <= lower_limit + proximity_threshold) or \
            (upper_limit - proximity_threshold <= value_float <= upper_limit)

    def update_table(self, params, limit_sensitivity):
        # Update the table widget with the new data
        self.tw_params.setRowCount(params.shape[0])
        self.tw_params.setColumnCount(params.shape[1])

        self.tw_params.setHorizontalHeaderLabels(params.columns.astype(str).tolist())
        self.tw_params.setVerticalHeaderLabels(params.index.astype(str).tolist())

        self.tw_params.resizeColumnsToContents()
        self.tw_params.resizeRowsToContents()

        # Create a dictionary to store limits for each parameter
        limits_dict = {}
        for param_name in params.index:
            lower_limit, upper_limit = self.parse_limits(param_name)
            limits_dict[param_name] = (lower_limit, upper_limit)
        print(limits_dict)

        for i in range(params.shape[1]):
            for j in range(params.shape[0]):
                value = params.iat[j, i]
                item = QTableWidgetItem()

                if isinstance(value, (float, int)):
                    # Format the value to two decimal places
                    formatted_value = format(value, ".2f")
                    item.setText(formatted_value)

                    # Get the limits from the dictionary
                    param_name = params.index[j]
                    lower_limit, upper_limit = limits_dict.get(param_name, (None, None))

                    if lower_limit is not None and upper_limit is not None:
                        # Check if the value is close to the limit
                        if self.is_close_to_limit(value, lower_limit, upper_limit, limit_sensitivity):
                            item.setBackground(QColor(249, 248, 113))  # Highlight in yellow
                            item.setForeground(QColor(0, 0, 0))
                        else:
                            item.setBackground(QColor(34, 48, 56))
                            item.setForeground(QColor(226, 220, 220))
                else:
                    item.setText(str(value))

                self.tw_params.setItem(j, i, item)
