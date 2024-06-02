from views.settings_window import SettingsWindow


class SettingsController:
    def __init__(self, app, model):
        self.model = model
        self.view = SettingsWindow(app)
        self.view.saved_button_clicked_signal.connect(self.save_settings)
        self.view.sb_limit_sensitivity.blockSignals(True)
        self.view.sb_timeframe.blockSignals(True)
        self.show_settings()
        self.view.sb_limit_sensitivity.blockSignals(False)
        self.view.sb_timeframe.blockSignals(False)

    def show_settings(self):
        settings = self.model.get_settings()
        self.view.set_settings(settings)

    def save_settings(self):
        setting_values = self.view.get_settings()
        self.model.save_settings(setting_values)
        self.view.pb_save.setEnabled(False)
