from PySide6.QtWidgets import QWidget, QListWidgetItem
from PySide6 import QtCore
from resources.ui.add_serials_window_ui import Ui_add_serials_window
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QStandardPaths


class AddSerialWindow(QWidget, Ui_add_serials_window):

    validate_signal = QtCore.Signal()
    delete_serials_signal = QtCore.Signal()
    clear_list_signal = QtCore.Signal()
    continue_signal = QtCore.Signal()
    import_signal = QtCore.Signal()
    go_to_info_signal = QtCore.Signal()
    #
    # Initializing the window for adding serials into the app
    def __init__(self, app):

        super().__init__()
        self.setupUi(self)
        self.app = app
        self.lw_serials.setItemAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        # When the user presses Return, clean the input, validate it and add it to the list
        self.le_serials.returnPressed.connect(self.validate_signal)

        # When the user clicks the delete button, delete the selected serials
        self.pb_delete.clicked.connect(self.delete_serials_signal)

        # When the user clicks the clear button, clear all serials from the list
        self.pb_clear.clicked.connect(self.clear_list_signal)

        self.lw_serials.itemClicked.connect(self.enable_delete_button)

        self.le_serials.textEdited.connect(self.disable_error_message_slot)

        self.pb_continue.clicked.connect(self.continue_signal)
        
        self.pb_import.clicked.connect(self.import_signal)
        
        self.pb_info.clicked.connect(self.go_to_info_signal)

    def get_input_from_user(self):
        return self.le_serials.text()

    #
    # Adding input from line edit to list view
    def add_serial(self, serial):
 
        # Converting the text to an item, for styling purposes
        item = QListWidgetItem(serial)
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
 
        self.lw_serials.addItem(item)
        self.switch_enabled_state(self.pb_clear, self.pb_continue, state_to_switch=True)
 
        # Clearing the line edit
        self.le_serials.clear()

    #
    # Delete selected serials from the list
    def delete_serials(self):

        items = self.lw_serials.selectedItems()

        # Check if there are any selected items
        if not items:
            return

        for item in items:
            self.lw_serials.takeItem(self.lw_serials.row(item))

            self.switch_enabled_state(
                self.pb_clear, self.pb_delete, self.pb_continue, state_to_switch=False
            )

        return items

    #
    # Clearing the serials list
    def clear_list(self):
        self.lw_serials.clear()
        self.switch_enabled_state(
            self.pb_clear, self.pb_delete, self.pb_continue, state_to_switch=False
        )

    #
    # Intermediary function due to Qt arhitecture
    def disable_error_message_slot(self):
        self.handle_error_message(False)

    #
    # Intermediary function due to Qt arhitecture
    def enable_delete_button(self):
        self.switch_enabled_state(self.pb_delete, state_to_switch=True)
        
    def get_excel_file_path(self):
        file_dialog = QFileDialog()
        downloads_path = QStandardPaths.writableLocation(
            QStandardPaths.DownloadLocation
        )
        file_dialog.setDirectory(downloads_path)
        file_path, _ = file_dialog.getOpenFileName(
            self, "Open Excel file", "", "Excel Files (*.xls *.xlsx)"
        )
        return file_path

    #
    # Handling the error message of invalid serial inputs
    def handle_error_message(self, state: bool, custom_message: str = None):

        # Checking if there is a custom message that we want to set the label to, otherwise let the default text be
        if custom_message is None:
            custom_message = "The serial entered is not valid! Please try another!"

        self.lb_error.setText(custom_message)

        self.switch_enabled_state(self.lb_error, state_to_switch=state)

        if state:
            self.le_serials.clear()

    #
    # Switch the state of a widget (or more) to a desired state, ex. if False, check first if the widget is not disabled alredy, and disabble it
    def switch_enabled_state(self, *widgets, state_to_switch: bool):
        for widget in widgets:
            if widget.isEnabled() is not state_to_switch:
                widget.setEnabled(state_to_switch)
