import json


class SettingsModel:
    def __init__(self):
        """
        Initialize the SettingsModel with default settings and limits, and load settings from file if available.
        """
        self.settings = {}  # Dictionary to hold settings
        self.DEFAULT_SETTINGS = {
            "limit_sensitivity": 20,
            "timeframe": 1,
            "input_priority": "normal",
            "other_priority": "normal",
        }  # Default settings
        self.sensitivity_limits = {"min": 0, "max": 100}  # Limits for sensitivity setting
        self.timeframe_limits = {"min": 1, "max": 8}  # Limits for timeframe setting

        self.priority_options = ["low", "normal", "high"]  # Priority options
        self._observers = []  # List of observers for notification
        self.load_settings()  # Load settings from file upon initialization

    def attach(self, observer):
        """
        Attach an observer to the model.

        Args:
            observer: The observer object to attach.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        Detach an observer from the model.

        Args:
            observer: The observer object to detach.
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        """
        Notify all attached observers of changes in the model's settings.
        """
        for observer in self._observers:
            observer.update(self)

    def load_settings(self):
        """
        Load settings from the 'settings.json' file. If file not found or settings are invalid, load default settings.
        """
        try:
            with open("settings.json", "r") as f:
                loaded_settings = json.load(f)  # Load settings from file
                if self.validate_settings(loaded_settings) == False:
                    self.save_settings(self.DEFAULT_SETTINGS)  # Save default settings if loaded settings are invalid
                else:
                    self.settings = loaded_settings  # Use loaded settings if valid
                self.notify()  # Notify observers of changes
        except FileNotFoundError:
            self.settings = self.DEFAULT_SETTINGS  # Use default settings if file not found

    def validate_settings(self, settings):
        """
        Validate settings against predefined limits and options.

        Args:
            settings (dict): The settings dictionary to validate.

        Returns:
            bool: True if settings are valid, False otherwise.
        """
        if not isinstance(settings["limit_sensitivity"], int) or not (
            self.sensitivity_limits.get("min")
            <= settings["limit_sensitivity"]
            <= self.sensitivity_limits.get("max")
        ):
            return False  # Check sensitivity limit validity
        if not isinstance(settings["timeframe"], int) or not (
            self.timeframe_limits.get("min")
            <= settings["timeframe"]
            <= self.timeframe_limits.get("max")
        ):
            return False  # Check timeframe limit validity
        if settings["input_priority"] not in self.priority_options:
            return False  # Check input priority validity
        if settings["other_priority"] not in self.priority_options:
            return False  # Check other priority validity
        return True  # Settings are valid

    def save_settings(self, settings):
        """
        Save settings to the 'settings.json' file.

        Args:
            settings (dict): The settings dictionary to save.
        """
        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=4)  # Write settings to file with indentation
            self.settings = settings  # Update current settings
            self.notify()  # Notify observers of changes

    def get_settings(self):
        """
        Get the current settings.

        Returns:
            dict: The current settings dictionary.
        """
        return self.settings  # Return current settings
