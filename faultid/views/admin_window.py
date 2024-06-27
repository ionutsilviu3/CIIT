from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QVBoxLayout, QApplication, QHeaderView
from PySide6 import QtCore
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from PySide6.QtGui import QPainter, QFont, QColor
from PySide6.QtCore import Qt
from resources.ui.admin_window_ui import Ui_admin_overview

class AdminWindow(QWidget, Ui_admin_overview):
    validate_signal = QtCore.Signal()  # Signal emitted for validating input email
    go_to_main_app_signal = QtCore.Signal()  # Signal emitted for navigating to the main application
    delete_user_signal = QtCore.Signal(str)  # Signal emitted for deleting a user (with email parameter)
    user_selected_signal = QtCore.Signal(str, str)  # Signal emitted when a user is selected (email, role)
    modify_role_signal = QtCore.Signal(str, str)  # Signal emitted for modifying a user's role (email, new role)

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)  # Set up the UI defined in Ui_admin_overview
        self.app = app

        # Initialize the table widget for displaying users
        self.tw_users.setMinimumWidth(300)
        self.tw_users.setColumnCount(2)
        self.tw_users.setHorizontalHeaderLabels(['Email', 'Role'])
        self.tw_users.horizontalHeader().setSectionsClickable(False)
        self.tw_users.setSelectionBehavior(QTableWidget.SelectRows)
        self.tw_users.verticalHeader().hide()
        self.tw_users.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tw_users.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tw_users.horizontalHeader().setStretchLastSection(True)  # Stretch the last section to fill the widget

        # Connect signals to slots
        self.le_users.returnPressed.connect(self.validate_signal)
        self.pb_delete.clicked.connect(self.on_delete_user_clicked)
        self.tw_users.itemClicked.connect(self.on_user_clicked)
        self.tw_users.itemSelectionChanged.connect(self.on_selection_changed)
        self.le_users.textEdited.connect(self.disable_error_message_slot)
        self.pb_add.clicked.connect(self.validate_signal)
        self.pb_modify_role.clicked.connect(self.on_modify_role_clicked)
        self.pb_main_app.clicked.connect(self.go_to_main_app_signal)

        # Initialize chart properties
        self.chart = QChart()
        self.chart.setTitle("User Roles Distribution")
        self.chart.setTitleFont(QFont("Roboto", 14, QFont.Bold))
        self.chart.setTitleBrush(QColor(226, 220, 220))
        self.chart.setBackgroundBrush(QColor(34, 48, 56))

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.vl_chart.addWidget(self.chart_view)  # Add chart view to the layout

        # Initialize button states
        self.pb_delete.setEnabled(False)
        self.pb_modify_role.setEnabled(False)

    def get_input(self):
        """
        Retrieve the input from the email line edit.

        Returns:
        - str: Input text from the line edit
        """
        return self.le_users.text()

    def set_users(self, users):
        """
        Populate the table widget with users.

        Parameters:
        - users: DataFrame containing 'Email' and 'Role' columns
        """
        self.tw_users.setRowCount(0)  # Clear existing rows
        for row_idx, (email, role) in users.iterrows():
            self.tw_users.insertRow(row_idx)
            email_item = QTableWidgetItem(email)
            role_item = QTableWidgetItem(role)
            self.tw_users.setItem(row_idx, 0, email_item)
            self.tw_users.setItem(row_idx, 1, role_item)
        self.tw_users.resizeColumnsToContents()  # Resize columns to fit content

    def on_user_clicked(self, item):
        """
        Slot triggered when a user is clicked in the table.

        Parameters:
        - item: QTableWidgetItem clicked
        """
        row = item.row()
        email_item = self.tw_users.item(row, 0)
        role_item = self.tw_users.item(row, 1)
        if email_item and role_item:
            email = email_item.text()
            role = role_item.text()
            self.user_selected_signal.emit(email, role)  # Emit signal with user email and role

    def on_selection_changed(self):
        """
        Slot triggered when the selection in the table widget changes.
        Enables or disables delete and modify role buttons based on the selected user's role.
        """
        selected_items = self.tw_users.selectedItems()
        if not selected_items:
            self.pb_delete.setEnabled(False)
            self.pb_modify_role.setEnabled(False)
        else:
            current_row = self.tw_users.currentRow()
            role_item = self.tw_users.item(current_row, 1)
            if role_item:
                current_role = role_item.text()
                if current_role != "Unregistered":
                    self.pb_delete.setEnabled(True)
                    self.pb_modify_role.setEnabled(True)
                else:
                    self.pb_delete.setEnabled(False)
                    self.pb_modify_role.setEnabled(False)

    def enable_modify_role_button(self, user_role):
        """
        Enable modify role button and set its text based on the user's current role.

        Parameters:
        - user_role: Current role of the user ("Manager", "Engineer", or "Unregistered")
        """
        if user_role == "Manager":
            self.pb_modify_role.setText("Remove manager role")
        elif user_role == "Engineer":
            self.pb_modify_role.setText("Turn into manager")
        else:
            self.pb_modify_role.setEnabled(False)
        self.pb_modify_role.setEnabled(True)

    def add_new_user(self, email):
        """
        Add a new user to the table widget.

        Parameters:
        - email: Email of the new user to be added
        """
        row_idx = self.tw_users.rowCount()
        self.tw_users.insertRow(row_idx)
        email_item = QTableWidgetItem(email)
        role_item = QTableWidgetItem("Unregistered")
        self.tw_users.setItem(row_idx, 0, email_item)
        self.tw_users.setItem(row_idx, 1, role_item)
        self.update_chart()  # Update the chart after adding a new user
        self.pb_add.setEnabled(False)
        self.tw_users.resizeColumnsToContents()  # Resize columns to fit content

    def delete_user(self, email):
        """
        Delete a user from the table widget.

        Parameters:
        - email: Email of the user to be deleted
        """
        for row_idx in range(self.tw_users.rowCount()):
            email_item = self.tw_users.item(row_idx, 0)
            if email_item and email_item.text() == email:
                self.tw_users.removeRow(row_idx)
                break
        self.update_chart()  # Update the chart after deleting a user

    def modify_user_role(self, email, new_role):
        """
        Modify the role of a user in the table widget.

        Parameters:
        - email: Email of the user whose role is to be modified
        - new_role: New role to assign to the user ("Engineer" or "Manager")
        """
        for row_idx in range(self.tw_users.rowCount()):
            email_item = self.tw_users.item(row_idx, 0)
            if email_item and email_item.text() == email:
                self.tw_users.setItem(row_idx, 1, QTableWidgetItem(new_role))
                break
        self.enable_modify_role_button(new_role)
        self.update_chart()  # Update the chart after modifying a user's role

    def on_delete_user_clicked(self):
        """
        Slot triggered when the delete user button is clicked.
        Deletes the selected user from the table.
        """
        selected_row = self.tw_users.currentRow()
        if selected_row != -1:
            email_item = self.tw_users.item(selected_row, 0)
            if email_item:
                email = email_item.text()
                self.delete_user_signal.emit(email)  # Emit signal to delete user

    def on_modify_role_clicked(self):
        """
        Slot triggered when the modify role button is clicked.
        Modifies the role of the selected user between "Engineer" and "Manager".
        """
        selected_row = self.tw_users.currentRow()
        if selected_row != -1:
            email_item = self.tw_users.item(selected_row, 0)
            role_item = self.tw_users.item(selected_row, 1)
            if email_item and role_item:
                email = email_item.text()
                current_role = role_item.text()
                new_role = "Engineer" if current_role == "Manager" else "Manager"
                self.modify_user_role(email, new_role)  # Modify user's role in the table
                self.modify_role_signal.emit(email, new_role)  # Emit signal to modify user's role

    def disable_error_message_slot(self):
        """
        Slot triggered when text in the email line edit is edited.
        Disables error message display and enables add user button.
        """
        self.handle_error_message(False)
        self.pb_add.setEnabled(True)

    def enable_delete_button(self):
        """Enable the delete user button."""
        self.pb_delete.setEnabled(True)

    def handle_error_message(self, state: bool, custom_message: str = None):
        """
        Display or hide an error message.

        Parameters:
        - state: True to display the message, False to hide it
        - custom_message: Custom error message to display (default is a generic message)
        """
        if custom_message is None:
            custom_message = "The email entered is not valid! Please try another!"

        self.lb_message.setText(custom_message)
        self.lb_message.setVisible(state)
        self.pb_add.setEnabled(False)  # Disable add user button on error

        if state:
            self.le_users.clear()  # Clear the email input on error

    def update_chart(self):
        """Update the chart showing user roles distribution."""
        role_counts = {}
        for row_idx in range(self.tw_users.rowCount()):
            role_item = self.tw_users.item(row_idx, 1)
            if role_item:
                role = role_item.text()
                if role in role_counts:
                    role_counts[role] += 1
                else:
                    role_counts[role] = 1

        series = QPieSeries()  # Create a new pie series for the chart
        custom_colors = {
            "Manager": QColor("#00AAB0"),  # Custom colors for different roles
            "Engineer": QColor("#00C598"),
            "Unregistered": QColor("#DD733F")
        }

        total_count = sum(role_counts.values())  # Total number of users

        for role, count in role_counts.items():
            slice = QPieSlice(role, count)  # Create a slice for each role
            if role in custom_colors:
                slice.setBrush(custom_colors[role])  # Set custom color for the slice
            percentage = (count / total_count) * 100  # Calculate percentage of users in this role
            slice.setLabel(f"{role} {percentage:.1f}%")  # Set label for the slice showing role and percentage
            slice.setLabelVisible(True)  # Make the label visible
            slice.setLabelFont(QFont("Roboto", 10))  # Set font for the label
            slice.setLabelBrush(QColor(226, 220, 220))  # Set brush (color) for the label text
            slice.hovered.connect(self.on_slice_hovered)  # Connect hover event of slice to slot
            series.append(slice)  # Add slice to the pie series

        self.chart.removeAllSeries()  # Remove all existing series from the chart
        self.chart.addSeries(series)  # Add the new series to the chart
        self.chart.setTitle("User Roles Distribution")  # Set title for the chart
        self.chart.legend().setVisible(True)  # Show legend for the chart
        self.chart.legend().setAlignment(Qt.AlignBottom)  # Align legend to the bottom
        self.chart.legend().setFont(QFont("Roboto", 10))  # Set font for the legend
        self.chart.legend().setLabelBrush(QColor(226, 220, 220))  # Set brush (color) for the legend text

        # Remove percentages from the legend
        for marker in self.chart.legend().markers(series):
            marker.setLabel(marker.label().split()[0])

        # Add animations to the chart series
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

    def on_slice_hovered(self, hovered):
        """
        Slot triggered when a pie slice is hovered over in the chart.

        Parameters:
        - hovered: True if the slice is hovered over, False otherwise
        """
        slice = self.sender()
        if hovered:
            slice.setExploded(True)  # Explode the slice when hovered over
            slice.setLabelVisible(True)  # Show label when hovered over
        else:
            slice.setExploded(False)  # Reset slice explosion when not hovered over
