import sys
import os
from enum import Enum
from dotenv import find_dotenv, load_dotenv

from models.settings_model import SettingsModel
from models.user_model import UserModel
from models.serial_model import SerialModel
from models.part_model import PartModel
from models.SQLClient import SQLClient
from models.query_master import QueryMaster

from controllers.settings_controller import SettingsController
from controllers.login_controller import LoginController
from controllers.admin_controller import AdminController
from controllers.add_serials_controller import AddSerialsController
from controllers.overview_controller import OverviewController
from controllers.advanced_overview_controller import AdvancedOverviewController

from PySide6.QtWidgets import QApplication, QStackedWidget

class Page(Enum):
    LOGIN = 0
    ADD_SERIALS = 1
    OVERVIEW = 2
    ADVANCED_OVERVIEW = 3
    ADMIN = 4
    SETTINGS = 5

class MainController:
    def __init__(self):
        self.app = QApplication(sys.argv)

        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        self.client = SQLClient(
            os.getenv("END_POINT"),
            os.getenv("PORT"),
            os.getenv("DB"),
            os.getenv("USER"),
            os.getenv("PASSWORD"),
        )
        self.query_master = QueryMaster()
        self.client.connect()

        self.settings_model = SettingsModel()
        self.user_model = UserModel(self.client, self.query_master)
        self.serial_model = SerialModel(self.client, self.query_master)
        self.part_model = PartModel(self.client, self.query_master, self.settings_model)

        # Create a QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setWindowTitle("FaultID")
        self.stacked_widget.setStyleSheet("background-color: rgb(34, 48, 56);")

        # Create the controllers and add their views to the QStackedWidget

        self.login_controller = LoginController(self.app, self.user_model)
        self.admin_controller = AdminController(self.app, self.user_model)
        self.add_serials_controller = AddSerialsController(
            self.app, self.serial_model
        )
        self.settings_controller = SettingsController(self.app, self.settings_model)
        self.overview_controller = OverviewController(
            self.app, self.part_model)

        self.advanced_overview_controller = AdvancedOverviewController(
            self.app, self.part_model
        )
        
        self.stacked_widget.addWidget(self.login_controller.view)
        self.stacked_widget.addWidget(self.add_serials_controller.view)
        self.stacked_widget.addWidget(self.overview_controller.view)
        self.stacked_widget.addWidget(self.advanced_overview_controller.view)
        self.stacked_widget.addWidget(self.admin_controller.view)
        self.stacked_widget.addWidget(self.settings_controller.view)

        # Mapping of pages
        self.page_mapping = {
            Page.LOGIN: self.login_controller.view,
            Page.ADD_SERIALS: self.add_serials_controller.view,
            Page.OVERVIEW: self.overview_controller.view,
            Page.ADVANCED_OVERVIEW: self.advanced_overview_controller.view,
            Page.ADMIN: self.admin_controller.view,
            Page.SETTINGS: self.settings_controller.view
        }

        # Initialize navigation history stack
        self.history_stack = []

        # Connect the signals
        self.login_controller.view.go_to_add_serials_signal.connect(
            lambda: self.switch_page(Page.ADD_SERIALS))
        
        self.login_controller.view.go_to_admin_signal.connect(
            lambda: self.switch_page(Page.ADMIN))
        
        self.login_controller.view.go_to_manager_signal.connect(
            self.switch_to_manager)
        
        self.add_serials_controller.view.continue_signal.connect(
            self.switch_windows)
        self.overview_controller.view.go_to_advanced_overview_signal.connect(
            lambda: self.switch_page(Page.ADVANCED_OVERVIEW)
        )
        self.overview_controller.view.go_to_settings_signal.connect(
            lambda: self.switch_page(Page.SETTINGS)
        )
        self.advanced_overview_controller.view.go_to_overview_signal.connect(
            lambda: self.switch_page(Page.OVERVIEW)
        )
        
        self.advanced_overview_controller.view.go_to_settings_signal.connect(
            lambda: self.switch_page(Page.SETTINGS)
        )
        self.settings_controller.view.go_to_previous_signal.connect(lambda: self.go_back())

        # Show the login window first
        self.switch_page(Page.LOGIN)
        self.stacked_widget.show()

        self.app.exec()

    def __del__(self):
        """
        Disconnects from the SQL client when the object is destroyed.
        """
        self.client.disconnect()
        self.cleanup_html_files()

    def cleanup_html_files(self):
        html_files = [f for f in os.listdir() if f.endswith('.html')]
        for file in html_files:
            os.remove(file)

    def switch_page(self, page: Page):
        # Add the current page to the history stack before switching
        if self.stacked_widget.currentIndex() != -1:
            current_page = Page(self.stacked_widget.currentIndex())
            self.history_stack.append(current_page)
        
        # Switch to the new page
        self.stacked_widget.setCurrentWidget(self.page_mapping[page])

    def go_back(self):
        if self.history_stack:
            previous_page = self.history_stack.pop()
            self.stacked_widget.setCurrentWidget(self.page_mapping[previous_page])

    def switch_windows(self):
        self.switch_page(Page.OVERVIEW)
        self.overview_controller.set_serials(
            self.add_serials_controller.get_serials())
        self.overview_controller.update_locations_filter()
        self.advanced_overview_controller.update_locations_filter()
        self.settings_model.notify()

    def switch_to_manager(self):
        pass
    
    def switch_to_info(self):
        pass