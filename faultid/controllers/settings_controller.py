from views.settings_window import SettingsWindow

class SettingsController:
    def __init__(self, app, model):
        """
        Initialize the SettingsController with the given application instance and model.

        Args:
            app: The application instance.
            model: The model instance that holds and manages settings data.
        """
        self.model = model  # Assign the model instance
        self.view = SettingsWindow(app)  # Create an instance of the SettingsWindow view
        self.view.saved_button_clicked_signal.connect(self.save_settings)  # Connect signal from view to save_settings method

        # Block signals temporarily to prevent unwanted signals during initialization
        self.view.sb_limit_sensitivity.blockSignals(True)
        self.view.sb_timeframe.blockSignals(True)

        self.show_settings()  # Show current settings in the view

        # Unblock signals after initialization
        self.view.sb_limit_sensitivity.blockSignals(False)
        self.view.sb_timeframe.blockSignals(False)

    def show_settings(self):
        """
        Show the current settings in the view.
        """
        settings = self.model.get_settings()  # Get current settings from the model
        self.view.set_settings(settings)  # Set settings in the view

    def save_settings(self):
        """
        Save settings from the view to the model.
        """
        setting_values = self.view.get_settings()  # Get settings values from the view
        self.model.save_settings(setting_values)  # Save settings to the model
        self.view.pb_save.setEnabled(False)  # Disable save button after saving settings
