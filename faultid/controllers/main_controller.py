import glob
from pathlib import Path
import sys
import os
from enum import Enum
from dotenv import find_dotenv, load_dotenv
from PySide6.QtWidgets import QApplication, QStackedWidget
from PySide6.QtGui import QIcon, QPixmap

from models.settings_model import SettingsModel
from models.user_model import UserModel
from models.serial_model import SerialModel
from models.part_model import PartModel
from models.SQLClient import SQLClient
from models.query_master import QueryMaster
from controllers.settings_controller import SettingsController
from controllers.login_controller import LoginController
from controllers.admin_controller import AdminController
from controllers.manager_controller import ManagerController
from controllers.add_serials_controller import AddSerialsController
from controllers.overview_controller import OverviewController
from controllers.advanced_overview_controller import AdvancedOverviewController
from views.info_window import InfoWindow
from views.contacts_window import ContactsWindow

# Enum to define different pages/views in the application
class Page(Enum):
    LOGIN = 0
    ADD_SERIALS = 1
    OVERVIEW = 2
    ADVANCED_OVERVIEW = 3
    ADMIN = 4
    MANAGER = 5
    SETTINGS = 6
    INFO = 7
    CONTACTS = 8

class MainController:
    def __init__(self):
        # Initialize the Qt Application
        self.app = QApplication(sys.argv)
        self.app.setWindowIcon(QIcon("app.ico"))
        # Load environment variables from .env file
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)


        # Initialize SQL client with environment variables
        self.client = SQLClient(
            os.getenv("END_POINT"),
            os.getenv("PORT"),
            os.getenv("DB"),
            os.getenv("USER"),
            os.getenv("PASSWORD"),
        )
        self.query_master = QueryMaster()
        self.client.connect()  # Connect to the database

        # Initialize models
        self.settings_model = SettingsModel()
        self.user_model = UserModel(self.client, self.query_master)
        self.serial_model = SerialModel(self.client, self.query_master)
        self.part_model = PartModel(self.client, self.query_master, self.settings_model)

        # Create the main stacked widget for managing views
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setWindowTitle("FaultID")
        self.stacked_widget.setStyleSheet("background-color: rgb(34, 48, 56);")

        # Initialize controllers and their respective views
        self.login_controller = LoginController(self.app, self.user_model)
        self.admin_controller = AdminController(self.app, self.user_model)
        self.manager_controller = ManagerController(self.app, self.user_model)
        self.add_serials_controller = AddSerialsController(self.app, self.serial_model)
        self.settings_controller = SettingsController(self.app, self.settings_model)
        self.overview_controller = OverviewController(self.app, self.part_model)
        self.advanced_overview_controller = AdvancedOverviewController(self.app, self.part_model)

        # Initialize standalone views
        self.info_view = InfoWindow(self.app)
        self.contacts_view = ContactsWindow(self.app)

        # Add views to the stacked widget
        self.stacked_widget.addWidget(self.login_controller.view)
        self.stacked_widget.addWidget(self.add_serials_controller.view)
        self.stacked_widget.addWidget(self.overview_controller.view)
        self.stacked_widget.addWidget(self.advanced_overview_controller.view)
        self.stacked_widget.addWidget(self.admin_controller.view)
        self.stacked_widget.addWidget(self.manager_controller.view)
        self.stacked_widget.addWidget(self.settings_controller.view)
        self.stacked_widget.addWidget(self.info_view)
        self.stacked_widget.addWidget(self.contacts_view)

        # Mapping pages to views
        self.page_mapping = {
            Page.LOGIN: self.login_controller.view,
            Page.ADD_SERIALS: self.add_serials_controller.view,
            Page.OVERVIEW: self.overview_controller.view,
            Page.ADVANCED_OVERVIEW: self.advanced_overview_controller.view,
            Page.ADMIN: self.admin_controller.view,
            Page.MANAGER: self.manager_controller.view,
            Page.SETTINGS: self.settings_controller.view,
            Page.INFO: self.info_view,
            Page.CONTACTS: self.contacts_view
        }

        # Initialize navigation history stack
        self.history_stack = []

        # Connect signals to slot functions for navigation
        self.connect_signals()

        # Show the login page first
        self.switch_page(Page.LOGIN)
        self.stacked_widget.show()
        
        # Start the Qt event loop
        self.app.exec()

    

    def switch_page(self, page: Page):
        """
        Switches the current view to the specified page.

        Args:
            page (Page): The page to switch to.
        """
        # Add the current page to the history stack before switching
        if self.stacked_widget.currentIndex() != -1:
            current_page = Page(self.stacked_widget.currentIndex())
            self.history_stack.append(current_page)
        
        # Switch to the new page
        self.stacked_widget.setCurrentWidget(self.page_mapping[page])

    def go_back(self):
        """
        Switches back to the previous page in the history stack.
        """
        if self.history_stack:
            previous_page = self.history_stack.pop()
            self.stacked_widget.setCurrentWidget(self.page_mapping[previous_page])

    def switch_windows(self):
        """
        Switches to the overview page after setting serials and updating filters.
        """
        self.overview_controller.set_serials(self.add_serials_controller.get_serials())
        self.overview_controller.update_locations_filter()
        self.advanced_overview_controller.update_locations_filter()
        self.settings_model.notify()
        self.switch_page(Page.OVERVIEW)

    def switch_to_admin(self):
        """
        Switches to the admin page and shows users.
        """
        self.admin_controller.show_users()
        self.switch_page(Page.ADMIN)

    def switch_to_manager(self):
        """
        Switches to the manager page and shows users.
        """
        self.manager_controller.show_users()
        self.switch_page(Page.MANAGER)

    def connect_signals(self):
        """
        Connects signals to corresponding slot functions for navigation.
        """
        self.login_controller.view.go_to_add_serials_signal.connect(
            lambda: self.switch_page(Page.ADD_SERIALS))
        self.login_controller.view.go_to_info_signal.connect(
            lambda: self.switch_page(Page.INFO))
        self.login_controller.view.go_to_admin_signal.connect(
            self.switch_to_admin)
        self.login_controller.view.go_to_manager_signal.connect(
            self.switch_to_manager)
        self.admin_controller.view.go_to_main_app_signal.connect(
            lambda: self.switch_page(Page.ADD_SERIALS))
        self.manager_controller.view.go_to_main_app_signal.connect(
            lambda: self.switch_page(Page.ADD_SERIALS))
        self.add_serials_controller.view.continue_signal.connect(
            self.switch_windows)
        self.add_serials_controller.view.go_to_info_signal.connect(
            lambda: self.switch_page(Page.INFO))
        self.overview_controller.view.go_to_advanced_overview_signal.connect(
            lambda: self.switch_page(Page.ADVANCED_OVERVIEW))
        self.overview_controller.view.go_to_settings_signal.connect(
            lambda: self.switch_page(Page.SETTINGS))
        self.overview_controller.view.go_to_info_signal.connect(
            lambda: self.switch_page(Page.INFO))
        self.advanced_overview_controller.view.go_to_overview_signal.connect(
            lambda: self.switch_page(Page.OVERVIEW))
        self.advanced_overview_controller.view.go_to_settings_signal.connect(
            lambda: self.switch_page(Page.SETTINGS))
        self.advanced_overview_controller.view.go_to_info_signal.connect(
            lambda: self.switch_page(Page.INFO))
        self.settings_controller.view.go_to_previous_signal.connect(
            lambda: self.go_back())
        self.info_view.go_to_contacts_signal.connect(
            lambda: self.switch_page(Page.CONTACTS))
        self.info_view.go_to_previous_signal.connect(
            lambda: self.go_back())
        self.contacts_view.go_to_previous_signal.connect(
            lambda: self.go_back())
