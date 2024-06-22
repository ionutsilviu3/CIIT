import re
import math
from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QTableWidgetItem
from PySide6 import QtCore
from PySide6.QtGui import QColor

from resources.ui.overview_window_ui import Ui_OverviewWidget

class OverviewWindow(QWidget, Ui_OverviewWidget):
    # Signals for UI interactions
    radio_button_clicked_signal = QtCore.Signal()
    go_to_advanced_overview_signal = QtCore.Signal()
    go_to_settings_signal = QtCore.Signal()
    go_to_info_signal = QtCore.Signal()
    
    def __init__(self, app):
        """
        Initialize the OverviewWindow with the given application instance.

        Args:
            app: The application instance.
        """
        super().__init__()
        self.setupUi(self)  # Setup UI defined in Ui_OverviewWidget
        self.app = app  # Store the application instance
        self.vb_locations = QVBoxLayout()  # Vertical layout for radio buttons
        self.vb_locations.setSpacing(16)  # Set spacing between radio buttons
        self.sa_contents_buttons.setLayout(self.vb_locations)  # Set layout for scroll area contents
        self.sa_radio_buttons.setWidget(self.sa_contents_buttons)  # Set widget for radio buttons scroll area
        self.tw_params.setCornerButtonEnabled(False)  # Disable corner button in table widget
        
        # Connect buttons to respective signals
        self.pb_advanced_overview.clicked.connect(self.go_to_advanced_overview_signal)
        self.pb_settings.clicked.connect(self.go_to_settings_signal)
        self.pb_info.clicked.connect(self.go_to_info_signal)

    def get_selected_location(self):
        """
        Get the selected location from radio buttons.

        Returns:
            str or None: The text of the selected radio button, or None if none selected.
        """
        radio_button = self.sender()
        if isinstance(radio_button, QRadioButton):
            if radio_button.isChecked():
                return radio_button.text()

    def update_radio_buttons(self, locations):
        """
        Update radio buttons with given locations.

        Args:
            locations (list): List of strings representing locations.
        """
        for loc in locations:
            radio_button = QRadioButton(loc)  # Create radio button for each location
            radio_button.clicked.connect(self.radio_button_clicked_signal)  # Connect signal for radio button click
            self.vb_locations.addWidget(radio_button)  # Add radio button to vertical layout

    def parse_limits(self, row_name):
        """
        Extract lower and upper limits from the row name using regular expression.

        Args:
            row_name (str): The name of the row containing limits in parentheses.

        Returns:
            tuple or None: Tuple of (lower_limit, upper_limit) or None if no limits found.
        """
        match = re.search(r'\(([^)]+)\)', row_name)  # Search for limits in parentheses
        if match:
            lower_limit, upper_limit = map(float, match.group(1).split(','))  # Split and convert limits to floats
            return lower_limit, upper_limit
        return None, None

    def is_close_to_limit(self, value, lower_limit, upper_limit, relative_sensitivity, absolute_sensitivity=0.1):
        """
        Check if a value is close to the specified limits.

        Args:
            value (float): The value to check.
            lower_limit (float): The lower limit.
            upper_limit (float): The upper limit.
            relative_sensitivity (float): The relative sensitivity factor.
            absolute_sensitivity (float, optional): The absolute sensitivity threshold. Defaults to 0.1.

        Returns:
            bool: True if value is close to the limits, False otherwise.
        """
        value_float = float(value)

        # Calculate proximity threshold as a percentage of the range
        proximity_threshold_relative = relative_sensitivity * (upper_limit - lower_limit)
        
        # Combine with an absolute threshold to handle small ranges
        proximity_threshold = max(proximity_threshold_relative, absolute_sensitivity)
        
        # Check if the value is close to the limits
        return (lower_limit <= value_float <= lower_limit + proximity_threshold) or \
            (upper_limit - proximity_threshold <= value_float <= upper_limit)

    def update_table(self, params, limit_sensitivity):
        """
        Update the table widget with parameters and highlight values close to limits.

        Args:
            params (DataFrame): The parameters data to display.
            limit_sensitivity (float): The sensitivity factor for highlighting values close to limits.
        """
        # Set the number of rows and columns in the table
        self.tw_params.setRowCount(params.shape[0])
        self.tw_params.setColumnCount(params.shape[1])

        # Set horizontal and vertical headers for the table
        self.tw_params.setHorizontalHeaderLabels(params.columns.astype(str).tolist())
        self.tw_params.setVerticalHeaderLabels(params.index.astype(str).tolist())

        # Resize columns and rows to fit content
        self.tw_params.resizeColumnsToContents()
        self.tw_params.resizeRowsToContents()

        # Create a dictionary to store limits for each parameter
        limits_dict = {}
        for param_name in params.index:
            lower_limit, upper_limit = self.parse_limits(param_name)
            limits_dict[param_name] = (lower_limit, upper_limit)

        # Iterate through each cell in the table
        for i in range(params.shape[1]):
            for j in range(params.shape[0]):
                value = params.iat[j, i]  # Get value from DataFrame cell
                item = QTableWidgetItem()  # Create QTableWidgetItem for cell

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
                            item.setForeground(QColor(0, 0, 0))  # Set text color to black
                        else:
                            item.setBackground(QColor(34, 48, 56))  # Set default background color
                            item.setForeground(QColor(226, 220, 220))  # Set text color to light gray
                else:
                    item.setText(str(value))  # Set text for non-numeric values

                self.tw_params.setItem(j, i, item)  # Set QTableWidgetItem in table widget
