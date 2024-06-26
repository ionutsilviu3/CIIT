from PySide6.QtWidgets import QWidget, QListWidgetItem, QFileDialog
from PySide6 import QtCore
from resources.ui.add_serials_window_ui import Ui_add_serials_window
from PySide6.QtCore import QStandardPaths


class AddSerialWindow(QWidget, Ui_add_serials_window):
    # Define signals for communication between components
    validate_signal = QtCore.Signal()
    delete_serials_signal = QtCore.Signal()
    clear_list_signal = QtCore.Signal()
    continue_signal = QtCore.Signal()
    import_signal = QtCore.Signal()
    go_to_info_signal = QtCore.Signal()

    # Initialize the window for adding serials into the app
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)  # Setup the UI defined in Ui_add_serials_window
        self.app = app  # Store the application reference
        self.lw_serials.setItemAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        # Connect signals and slots
        self.le_serials.returnPressed.connect(self.validate_signal)
        self.pb_delete.clicked.connect(self.delete_serials_signal)
        self.pb_clear.clicked.connect(self.clear_list_signal)
        self.lw_serials.itemClicked.connect(self.enable_delete_button)
        self.le_serials.textEdited.connect(self.disable_error_message_slot)
        self.pb_continue.clicked.connect(self.continue_signal)
        self.pb_import.clicked.connect(self.import_signal)
        self.pb_info.clicked.connect(self.go_to_info_signal)

    # Get the input text from the line edit widget
    def get_input_from_user(self):
        return self.le_serials.text()

    # Add a serial to the list view
    def add_serial(self, serial):
        item = QListWidgetItem(serial)  # Create a list item with the serial text
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)  # Center-align the text
        self.lw_serials.addItem(item)  # Add the item to the list widget
        # Enable buttons and clear line edit
        self.switch_enabled_state(self.pb_clear, self.pb_continue, state_to_switch=True)
        self.le_serials.clear()  # Clear the line edit after adding

    # Delete selected serials from the list view
    def delete_serials(self):
        items = self.lw_serials.selectedItems()  # Get selected items
        if not items:  # If no items are selected, return
            return
        for item in items:
            self.lw_serials.takeItem(self.lw_serials.row(item))  # Remove item from list
        # Disable buttons as appropriate
        self.switch_enabled_state(self.pb_clear, self.pb_delete, self.pb_continue, state_to_switch=False)
        return items  # Return the deleted items

    # Clear all serials from the list view
    def clear_list(self):
        self.lw_serials.clear()  # Clear all items from the list
        self.switch_enabled_state(self.pb_clear, self.pb_delete, self.pb_continue, state_to_switch=False)

    # Slot to disable error message handling
    def disable_error_message_slot(self):
        self.handle_error_message(False)

    # Slot to enable delete button when an item is clicked
    def enable_delete_button(self):
        self.switch_enabled_state(self.pb_delete, state_to_switch=True)

    # Get the path of an Excel file selected by the user
    def get_excel_file_path(self):
        file_dialog = QFileDialog()  # Create file dialog instance
        downloads_path = QStandardPaths.writableLocation(QStandardPaths.DownloadLocation)  # Get downloads path
        file_dialog.setDirectory(downloads_path)  # Set initial directory for file dialog
        file_path, _ = file_dialog.getOpenFileName(self, "Open Excel file", "", "Excel Files (*.xls *.xlsx)")  # Get file path
        return file_path  # Return the selected file path

    # Handle error messages for invalid serial inputs
    def handle_error_message(self, state: bool, custom_message: str = None):
        if custom_message is None:
            custom_message = "The serial entered is not valid! Please try another!"
        self.lb_error.setText(custom_message)  # Set error message text
        self.switch_enabled_state(self.lb_error, state_to_switch=state)  # Enable/disable error label
        if state:
            self.le_serials.clear()  # Clear line edit on error state

    # Toggle enabled state of widgets based on state_to_switch parameter
    def switch_enabled_state(self, *widgets, state_to_switch: bool):
        for widget in widgets:
            if widget.isEnabled() is not state_to_switch:
                widget.setEnabled(state_to_switch)
