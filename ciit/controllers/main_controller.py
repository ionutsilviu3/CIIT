import sys
import os
from dotenv import find_dotenv, load_dotenv
from models.serial_model import SerialModel
from models.login_model import LoginModel
from models.part_model import PartModel
from models.query_master import QueryMaster
from models.SQLClient import SQLClient
from controllers.login_controller import LoginController
from controllers.add_serials_controller import AddSerialsController
from controllers.overview_controller import OverviewController
from controllers.advanced_overview_controller import AdvancedOverviewController
from PySide6.QtWidgets import QApplication, QStackedWidget


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

        self.login_model = LoginModel(self.client, self.query_master)
        self.serial_model = SerialModel(self.client, self.query_master)
        self.part_model = PartModel(self.client, self.query_master)

        # Create a QStackedWidget
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.setWindowTitle("FaultID")
        self.stacked_widget.setStyleSheet("background-color: rgb(34, 48, 56);")

        # Create the controllers and add their views to the QStackedWidget

        self.login_controller = LoginController(self.app, self.login_model)

        self.add_serials_controller = AddSerialsController(
            self.app, self.serial_model
        )

        self.overview_controller = OverviewController(
            self.app, self.part_model)

        self.advanced_overview_controller = AdvancedOverviewController(
            self.app, self.part_model
        )

        self.stacked_widget.addWidget(self.login_controller.view)
        self.stacked_widget.addWidget(self.add_serials_controller.view)
        self.stacked_widget.addWidget(self.overview_controller.view)
        self.stacked_widget.addWidget(self.advanced_overview_controller.view)

        # Connect the signals
        self.login_controller.view.go_to_add_serials_signal.connect(
            self.switch_to_add_serials)
        self.add_serials_controller.view.continue_signal.connect(
            self.switch_windows)
        self.overview_controller.view.go_to_advanced_overview_signal.connect(
            self.switch_to_advanced
        )
        self.advanced_overview_controller.view.go_to_overview_signal.connect(
            self.switch_to_overview
        )

        # Show the login window first
        self.stacked_widget.setCurrentIndex(0)
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

    def switch_to_add_serials(self):
        self.stacked_widget.setCurrentIndex(1)

    def switch_windows(self):
        # Switch to the next window in the QStackedWidget
        self.stacked_widget.setCurrentIndex(2)

        self.overview_controller.set_serials(
            self.add_serials_controller.get_serials())
        self.overview_controller.update_locations_filter()
        self.advanced_overview_controller.update_locations_filter()

    def switch_to_overview(self):
        self.stacked_widget.setCurrentIndex(2)

    def switch_to_advanced(self):
        self.stacked_widget.setCurrentIndex(3)
