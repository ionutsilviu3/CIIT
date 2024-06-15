from PySide6.QtWidgets import QWidget, QTableWidgetItem, QTableWidget, QVBoxLayout, QApplication
from PySide6 import QtCore
from PySide6.QtCharts import QChart, QChartView, QPieSeries, QPieSlice
from PySide6.QtGui import QPainter, QFont, QColor
from PySide6.QtCore import Qt
from views.admin_window import AdminWindow

class ManagerWindow(AdminWindow):
    def __init__(self, app):
        super().__init__(app)
        self.pb_modify_role.hide()  # Hide the modify role button
        self.lb_title.setText("Manager")

    def on_selection_changed(self):
        selected_items = self.tw_users.selectedItems()
        if not selected_items:
            self.pb_delete.setEnabled(False)
        else:
            current_row = self.tw_users.currentRow()
            role_item = self.tw_users.item(current_row, 1)
            if role_item:
                current_role = role_item.text()
                if current_role != "Unregistred":
                    self.pb_delete.setEnabled(True)
                else:
                    self.pb_delete.setEnabled(False)

    def on_modify_role_clicked(self):
        pass  # Override to do nothing