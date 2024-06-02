from PySide6.QtWidgets import QWidget
from resources.ui.settings_window_ui import Ui_settings_window
from PySide6 import QtCore


class SettingsWindow(QWidget, Ui_settings_window):

    go_to_previous_signal = QtCore.Signal()
    saved_button_clicked_signal = QtCore.Signal()

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.pb_back.clicked.connect(self.go_to_previous_signal)
        self.pb_save.clicked.connect(self.saved_button_clicked_signal)

        self.sb_limit_sensitivity.valueChanged.connect(self.show_saved_button)
        self.sb_timeframe.valueChanged.connect(self.show_saved_button)
        self.rb_low_input.clicked.connect(self.show_saved_button)
        self.rb_normal_input.clicked.connect(self.show_saved_button)
        self.rb_high_input.clicked.connect(self.show_saved_button)
        self.rb_low_other.clicked.connect(self.show_saved_button)
        self.rb_normal_other.clicked.connect(self.show_saved_button)
        self.rb_high_other.clicked.connect(self.show_saved_button)

    def show_saved_button(self):
        self.pb_save.setEnabled(True)

    def get_settings(self):
        return {
            "limit_sensitivity": self.sb_limit_sensitivity.value(),
            "timeframe": self.sb_timeframe.value(),
            "input_priority": self.get_input_priority(),
            "other_priority": self.get_other_priority(),
        }

    def set_input_priority(self, priority):
        if priority == "low":
            self.rb_low_input.setChecked(True)
        elif priority == "high":
            self.rb_high_input.setChecked(True)
        else:
            self.rb_normal_input.setChecked(True)

    def set_other_priority(self, priority):
        if priority == "low":
            self.rb_low_other.setChecked(True)
        elif priority == "high":
            self.rb_normal_other.setChecked(True)
        else:
            self.rb_normal_other.setChecked(True)

    def get_input_priority(self):
        if self.rb_low_input.isChecked():
            return "low"
        elif self.rb_normal_input.isChecked():
            return "normal"
        else:
            return "high"

    def get_other_priority(self):
        if self.rb_low_other.isChecked():
            return "low"
        elif self.rb_normal_other.isChecked():
            return "normal"
        else:
            return "high"

    def set_settings(self, settings):
        self.sb_limit_sensitivity.setValue(settings["limit_sensitivity"])
        self.sb_timeframe.setValue(settings["timeframe"])
        self.set_input_priority(settings["input_priority"])
        self.set_other_priority(settings["other_priority"])
