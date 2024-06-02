import os
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Slot, Signal, QDir
from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QFileDialog
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy.spatial import distance

from resources.ui.advanced_overview_window_ui import Ui_AdvancedOverviewWidget

class AdvancedOverviewWindow(QWidget, Ui_AdvancedOverviewWidget):
    radio_button_clicked_signal = Signal()
    go_to_overview_signal = Signal()
    go_to_settings_signal = Signal()
    export_data_signal = Signal()
    
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)
        self.app = app
        self.vb_locations = QVBoxLayout()
        self.vb_locations.setSpacing(14)
        self.vb_plots.setSpacing(14)
        self.sa_contents_buttons.setLayout(self.vb_locations)
        self.sa_radio_buttons.setWidget(self.sa_contents_buttons)
        self.pb_overview.clicked.connect(self.go_to_overview_signal.emit)
        self.pb_settings.clicked.connect(self.go_to_settings_signal)
        self.pb_export.clicked.connect(self.export_data_signal)
        self.views = {}
        self.selected_location = None
        self.locations_radio_buttons = []

    @Slot()
    def get_selected_location(self):
        for radio_button in self.locations_radio_buttons:
            if radio_button.isChecked():
                self.selected_location = radio_button.text()
                return self.selected_location

    @Slot()
    def update_radio_buttons(self, locations):
        for loc in locations:
            radio_button = QRadioButton(loc)
            radio_button.clicked.connect(self.radio_button_clicked_signal)
            self.vb_locations.addWidget(radio_button)
            self.locations_radio_buttons.append(radio_button)
    
    def clear_plots(self):
        # Clear existing plots
        while self.vb_plots.count():
            item = self.vb_plots.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
    
    def create_plot(self, parameter, other_parts_param, input_parts_param, blue_outliers, parameter_limits):
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        fig.add_trace(
            go.Scatter(
                x=other_parts_param["created_at"],
                y=other_parts_param["value"],
                mode="markers",
                marker=dict(color='blue'),
                name="Parts Produced",
                text=other_parts_param["unit_serial_number"],
            ),
            secondary_y=False,
        )

        if np.any(blue_outliers):
            fig.add_trace(
                go.Scatter(
                    x=other_parts_param[blue_outliers]["created_at"],
                    y=other_parts_param[blue_outliers]["value"],
                    mode="markers",
                    marker=dict(color='yellow', line=dict(width=1, color='gray')),
                    name="Outlier Parts Produced",
                    text=other_parts_param[blue_outliers]["unit_serial_number"],
                ),
                secondary_y=False,
            )

        fig.add_trace(
            go.Scatter(
                x=input_parts_param["created_at"],
                y=input_parts_param["value"],
                mode="markers",
                marker=dict(color="red"),
                name="Input Parts",
                text=input_parts_param["unit_serial_number"],
            ),
            secondary_y=False,
        )

        fig.add_trace(
            go.Scatter(
                x=[other_parts_param["created_at"].min(), other_parts_param["created_at"].max()],
                y=[parameter_limits["lower_limit"], parameter_limits["lower_limit"]],
                mode="lines",
                line=dict(color="navy", width=2, dash="dash"),
                name="Lower Limit",
                showlegend=True,
            ),
            secondary_y=False,
        )
        fig.add_trace(
            go.Scatter(
                x=[other_parts_param["created_at"].min(), other_parts_param["created_at"].max()],
                y=[parameter_limits["upper_limit"], parameter_limits["upper_limit"]],
                mode="lines",
                line=dict(color="navy", width=2, dash="dash"),
                name="Upper Limit",
                showlegend=True,
            ),
            secondary_y=False,
        )

        fig.update_layout(
            title_text=f"Scatter Plot of {parameter} Value Over Time",
            xaxis_title="Time (days since start)",
            yaxis_title="Parameter Value",
            legend_title="Legend",
            legend=dict(itemsizing='constant'),
        )

        file_path = os.path.join(os.getcwd(), f"temp_plot_{parameter}.html")
        fig.write_html(file_path)

        view = QWebEngineView()
        view.setFixedSize(800, 600)
        view.load(QUrl.fromLocalFile(file_path))

        self.vb_plots.addWidget(view)
        
    def get_export_path(self):
        options = QFileDialog.Options()
        # Remove DontUseNativeDialog option to use the native dialog
        # options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(
            self,
            "Export Data",
            QDir.homePath() + "/Downloads/FaultID_Export.xlsx",
            "Excel File (*.xlsx);;All Files (*)",
            options=options
        )
        return file_path