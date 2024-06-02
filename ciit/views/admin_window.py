from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QVBoxLayout, QApplication
from PySide6 import QtCore
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from PySide6.QtGui import QPainter, QFont, QColor
from PySide6.QtCore import Qt
from resources.ui.admin_window_ui import Ui_admin_overview


class AdminWindow(QWidget, Ui_admin_overview):

    validate_signal = QtCore.Signal()
    delete_user_signal = QtCore.Signal(str)  # emit the email of the user to delete
    user_selected_signal = QtCore.Signal(str, str)  # emit email and role

    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        
        self.tw_users.setColumnCount(2)
        self.tw_users.setAlternatingRowColors(True)
        self.tw_users.setHorizontalHeaderLabels(['Email', 'Role'])
        self.tw_users.horizontalHeader().setSectionsClickable(False)
        self.tw_users.setSelectionBehavior(QTableWidget.SelectRows)
        self.tw_users.verticalHeader().hide()

        self.le_users.returnPressed.connect(self.validate_signal)
        self.pb_delete.clicked.connect(self.on_delete_user_clicked)
        self.tw_users.itemClicked.connect(self.on_user_clicked)
        self.tw_users.itemSelectionChanged.connect(self.on_selection_changed)
        self.le_users.textEdited.connect(self.disable_error_message_slot)
        self.pb_add.clicked.connect(self.validate_signal)
        self.pb_modify_role.clicked.connect(self.on_modify_role_clicked)

        # Initially disable the delete and modify buttons
        self.pb_delete.setEnabled(False)
        self.pb_modify_role.setEnabled(False)
        
        # Set up the pie chart
        self.chart = QChart()
        self.chart.setTitle("User Roles Distribution")
        self.chart.setTitleFont(QFont("Arial", 14, QFont.Bold))
        self.chart.setTitleBrush(QColor("darkblue"))
        self.chart.setBackgroundBrush(QColor("white"))

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        
        self.vl_chart.addWidget(self.chart_view)
        
        self.update_chart()

    def get_input(self):
        return self.le_users.text()

    def set_users(self, users):
        self.tw_users.setRowCount(0)  # Clear existing rows
        for row_idx, (email, role) in users.iterrows():
            self.tw_users.insertRow(row_idx)
            email_item = QTableWidgetItem(email)
            role_item = QTableWidgetItem(role)
            self.tw_users.setItem(row_idx, 0, email_item)
            self.tw_users.setItem(row_idx, 1, role_item)
    
    def on_user_clicked(self, item):
        row = item.row()
        email_item = self.tw_users.item(row, 0)
        role_item = self.tw_users.item(row, 1)
        if email_item and role_item:
            email = email_item.text()
            role = role_item.text()
            self.user_selected_signal.emit(email, role)
    
    def on_selection_changed(self):
        selected_items = self.tw_users.selectedItems()
        if not selected_items:
            self.pb_delete.setEnabled(False)
            self.pb_modify_role.setEnabled(False)

    def enable_modify_role_button(self, user_role):
        if user_role == "Manager":
            self.pb_modify_role.setText("Remove manager role")
        elif user_role == "Engineer":
            self.pb_modify_role.setText("Turn into manager")
        self.pb_modify_role.setEnabled(True)
    
    def add_new_user(self, email):
        row_idx = self.tw_users.rowCount()
        self.tw_users.insertRow(row_idx)
        email_item = QTableWidgetItem(email)
        role_item = QTableWidgetItem("Unregistred")
        self.tw_users.setItem(row_idx, 0, email_item)
        self.tw_users.setItem(row_idx, 1, role_item)
        self.update_chart()

    def delete_user(self, email):
        for row_idx in range(self.tw_users.rowCount()):
            email_item = self.tw_users.item(row_idx, 0)
            if email_item and email_item.text() == email:
                self.tw_users.removeRow(row_idx)
                break
        self.update_chart()

    def modify_user_role(self, email, new_role):
        for row_idx in range(self.tw_users.rowCount()):
            email_item = self.tw_users.item(row_idx, 0)
            if email_item and email_item.text() == email:
                self.tw_users.setItem(row_idx, 1, QTableWidgetItem(new_role))
                break
        self.update_chart()

    def on_delete_user_clicked(self):
        selected_row = self.tw_users.currentRow()
        if selected_row != -1:
            email_item = self.tw_users.item(selected_row, 0)
            if email_item:
                email = email_item.text()
                self.delete_user_signal.emit(email)
    
    def on_modify_role_clicked(self):
        selected_row = self.tw_users.currentRow()
        if selected_row != -1:
            email_item = self.tw_users.item(selected_row, 0)
            role_item = self.tw_users.item(selected_row, 1)
            if email_item and role_item:
                email = email_item.text()
                current_role = role_item.text()
                new_role = "Engineer" if current_role == "Manager" else "Manager"
                self.modify_user_role(email, new_role)
                # Directly call controller method if needed to update model
    
    def disable_error_message_slot(self):
        self.handle_error_message(False)

    def enable_delete_button(self):
        self.pb_delete.setEnabled(True)

    def handle_error_message(self, state: bool, custom_message: str = None):
        if custom_message is None:
            custom_message = "The email entered is not valid! Please try another!"

        self.lb_message.setText(custom_message)
        self.lb_message.setVisible(state)

        if state:
            self.le_users.clear()

    def switch_enabled_state(self, *widgets, state_to_switch: bool):
        for widget in widgets:
            widget.setEnabled(state_to_switch)

    def update_chart(self):
        role_counts = {}
        for row_idx in range(self.tw_users.rowCount()):
            role_item = self.tw_users.item(row_idx, 1)
            if role_item:
                role = role_item.text()
                if role in role_counts:
                    role_counts[role] += 1
                else:
                    role_counts[role] = 1

        series = QPieSeries()
        custom_colors = {
            "Manager": QColor("#4caf50"),  # Green
            "Engineer": QColor("#2196f3"),  # Blue
            "Unregistered": QColor("#f44336")  # Red
        }

        total_count = sum(role_counts.values())

        for role, count in role_counts.items():
            slice = QPieSlice(role, count)
            if role in custom_colors:
                slice.setBrush(custom_colors[role])
            percentage = (count / total_count) * 100
            slice.setLabel(f"{role} {percentage:.1f}%")
            slice.setLabelVisible(True)
            slice.hovered.connect(self.on_slice_hovered)
            series.append(slice)

        self.chart.removeAllSeries()
        self.chart.addSeries(series)
        self.chart.setTitle("User Roles Distribution")
        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)
        self.chart.legend().setFont(QFont("Arial", 10))
        self.chart.legend().setLabelBrush(QColor("darkblue"))

        # Remove percentages from the legend
        for marker in self.chart.legend().markers(series):
            marker.setLabel(marker.label().split()[0])

        # Add animations
        self.chart.setAnimationOptions(QChart.SeriesAnimations)

        # Add shadow effect
        self.chart.setDropShadowEnabled(True)

    def on_slice_hovered(self, hovered):
        slice = self.sender()
        if hovered:
            slice.setExploded(True)
            slice.setLabelVisible(True)
        else:
            slice.setExploded(False)