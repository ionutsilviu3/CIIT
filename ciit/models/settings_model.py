import json


class SettingsModel:

    def __init__(self):
        self.settings = {}
        self.DEFAULT_SETTINGS = {
            "limit_sensitivity": 5,
            "timeframe": 1,
            "input_priority": "normal",
            "other_priority": "normal",
        }
        self.sensitivity_limits = {"min": 0, "max": 100}
        self.timeframe_limits = {"min": 1, "max": 8}

        self.priority_options = ["low", "normal", "high"]
        self._observers = []
        self.load_settings()

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                loaded_settings = json.load(f)
                if self.validate_settings(loaded_settings) == False:
                    self.save_settings(self.DEFAULT_SETTINGS)
                else:
                    self.settings = loaded_settings
                self.notify()
        except FileNotFoundError:
            self.settings = self.DEFAULT_SETTINGS

    def validate_settings(self, settings):
        if not isinstance(settings["limit_sensitivity"], int) or not (
            self.sensitivity_limits.get("min")
            <= settings["limit_sensitivity"]
            <= self.sensitivity_limits.get("max")
        ):
            return False
        if not isinstance(settings["timeframe"], int) or not (
            self.timeframe_limits.get("min")
            <= settings["timeframe"]
            <= self.timeframe_limits.get("max")
        ):
            return False
        if settings["input_priority"] not in self.priority_options:
            return False
        if settings["other_priority"] not in self.priority_options:
            return False
        return True

    def save_settings(self, settings):
        with open("settings.json", "w") as f:
            json.dump(settings, f, indent=4)
            self.settings = settings
            self.notify()

    def get_settings(self):
        return self.settings
