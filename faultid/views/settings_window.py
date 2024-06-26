from PySide6.QtWidgets import QWidget
from resources.ui.settings_window_ui import Ui_settings_window
from PySide6 import QtCore

class SettingsWindow(QWidget, Ui_settings_window):
   
    go_to_previous_signal = QtCore.Signal()  # Signal to go to the previous window
    saved_button_clicked_signal = QtCore.Signal()  # Signal emitted when the save button is clicked

    def __init__(self, app):
        """
        Initialize the SettingsWindow.

        Args:
            app: The application instance.
        """
        super().__init__()
        self.setupUi(self)  # Setup UI defined in Ui_settings_window
        self.app = app  # Store the application instance

        # Connect signals to their respective slots
        self.pb_back.clicked.connect(self.go_to_previous_signal)  # Connect back button to go_to_previous_signal
        self.pb_save.clicked.connect(self.saved_button_clicked_signal)  # Connect save button to saved_button_clicked_signal

        # Connect value changed signals to show_saved_button method
        self.sb_limit_sensitivity.valueChanged.connect(self.show_saved_button)
        self.sb_timeframe.valueChanged.connect(self.show_saved_button)
        self.rb_low_input.clicked.connect(self.show_saved_button)
        self.rb_normal_input.clicked.connect(self.show_saved_button)
        self.rb_high_input.clicked.connect(self.show_saved_button)
        self.rb_low_other.clicked.connect(self.show_saved_button)
        self.rb_normal_other.clicked.connect(self.show_saved_button)
        self.rb_high_other.clicked.connect(self.show_saved_button)

    def show_saved_button(self):
        """
        Enable the save button when settings are changed.
        """
        self.pb_save.setEnabled(True)

    def get_settings(self):
        """
        Get the current settings from the UI.

        Returns:
            dict: A dictionary containing the current settings.
        """
        return {
            "limit_sensitivity": self.sb_limit_sensitivity.value(),
            "timeframe": self.sb_timeframe.value(),
            "input_priority": self.get_input_priority(),
            "other_priority": self.get_other_priority(),
        }

    def set_input_priority(self, priority):
        """
        Set the input priority radio buttons based on the provided priority.

        Args:
            priority (str): The input priority ("low", "normal", or "high").
        """
        if priority == "low":
            self.rb_low_input.setChecked(True)
        elif priority == "high":
            self.rb_high_input.setChecked(True)
        else:
            self.rb_normal_input.setChecked(True)

    def set_other_priority(self, priority):
        """
        Set the other priority radio buttons based on the provided priority.

        Args:
            priority (str): The other priority ("low", "normal", or "high").
        """
        if priority == "low":
            self.rb_low_other.setChecked(True)
        elif priority == "high":
            self.rb_high_other.setChecked(True)
        else:
            self.rb_normal_other.setChecked(True)

    def get_input_priority(self):
        """
        Get the current input priority selected by the user.

        Returns:
            str: The current input priority ("low", "normal", or "high").
        """
        if self.rb_low_input.isChecked():
            return "low"
        elif self.rb_normal_input.isChecked():
            return "normal"
        else:
            return "high"

    def get_other_priority(self):
        """
        Get the current other priority selected by the user.

        Returns:
            str: The current other priority ("low", "normal", or "high").
        """
        if self.rb_low_other.isChecked():
            return "low"
        elif self.rb_normal_other.isChecked():
            return "normal"
        else:
            return "high"

    def set_settings(self, settings):
        """
        Set the UI elements to display the provided settings.

        Args:
            settings (dict): A dictionary containing the settings to display.
        """
        self.sb_limit_sensitivity.setValue(settings["limit_sensitivity"])
        self.sb_timeframe.setValue(settings["timeframe"])
        self.set_input_priority(settings["input_priority"])
        self.set_other_priority(settings["other_priority"])
