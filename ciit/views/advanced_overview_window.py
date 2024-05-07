import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton
from PySide6 import QtCore
from resources.ui.advanced_overview_window_ui import Ui_AdvancedOverviewWidget
 
 
class AdvancedOverviewWindow(QWidget, Ui_AdvancedOverviewWidget):
    radio_button_clicked_signal = QtCore.Signal()
    go_to_overview_signal = QtCore.Signal()
 
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
 
    def get_selected_location(self):
        radio_button = self.sender()
        if isinstance(radio_button, QRadioButton):
            if radio_button.isChecked():
                return radio_button.text()
 
    def update_radio_buttons(self, locations):
        for loc in locations:
            radio_button = QRadioButton(loc)
            radio_button.clicked.connect(self.radio_button_clicked_signal)
            self.vb_locations.addWidget(radio_button)
 
    def update_plots(self, input_parts, other_parts):
        parameters = list(set(input_parts["name"]))

        for parameter in parameters:
            other_parts_param = other_parts[other_parts["name"] == parameter]
            input_parts_param = input_parts[input_parts["name"] == parameter]

            # Get the limits for the current parameter
            parameter_limits = input_parts_param.iloc[0][["lower_limit", "upper_limit"]]

            # Create a scatter plot with Plotly
            fig = make_subplots(specs=[[{"secondary_y": True}]])

            fig.add_trace(
                go.Scatter(
                    x=other_parts_param["created_at"],
                    y=other_parts_param["value"],
                    mode="markers",
                    marker=dict(color="blue"),
                    name="Parts Produced",
                    text=other_parts_param["unit_serial_number"],
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
                secondary_y=True,
            )

            # Add horizontal lines for the lower and upper limits
            fig.add_shape(
                type="line",
                x0=input_parts_param["created_at"].min(),
                y0=parameter_limits["lower_limit"],
                x1=input_parts_param["created_at"].max(),
                y1=parameter_limits["lower_limit"],
                line=dict(color="green", width=2, dash="dash"),
                secondary_y=True,
            )
            fig.add_shape(
                type="line",
                x0=input_parts_param["created_at"].min(),
                y0=parameter_limits["upper_limit"],
                x1=input_parts_param["created_at"].max(),
                y1=parameter_limits["upper_limit"],
                line=dict(color="red", width=2, dash="dash"),
                secondary_y=True,
            )

            fig.update_layout(
                title_text=f"Scatter Plot of {parameter} Value Over Time",
                xaxis_title="Time (days since start)",
                yaxis_title="Parameter Value",
            )

            # Get the absolute path of the current directory
            current_dir = os.getcwd()

            # Create the absolute path of the HTML file
            file_path = os.path.join(current_dir, f"temp_plot_{parameter}.html")

            # Convert the plot to HTML and save it
            fig.write_html(file_path)

            # Create a QWebEngineView
            view = QWebEngineView()
            view.setFixedSize(800, 600)
            # Load the HTML file
            view.load(QUrl.fromLocalFile(file_path))

            # Add the QWebEngineView to the QVBoxLayout
            self.vb_plots.addWidget(view)


