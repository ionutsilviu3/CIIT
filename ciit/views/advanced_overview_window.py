import os
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Slot, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from scipy.spatial import distance

from resources.ui.advanced_overview_window_ui import Ui_AdvancedOverviewWidget

class AdvancedOverviewWindow(QWidget, Ui_AdvancedOverviewWidget):
    radio_button_clicked_signal = Signal()
    go_to_overview_signal = Signal()

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
        self.views = {}

    @Slot()
    def get_selected_location(self):
        radio_button = self.sender()
        if isinstance(radio_button, QRadioButton):
            if radio_button.isChecked():
                return radio_button.text()

    @Slot()
    def update_radio_buttons(self, locations):
        for loc in locations:
            radio_button = QRadioButton(loc)
            radio_button.clicked.connect(self.radio_button_clicked_signal)
            self.vb_locations.addWidget(radio_button)

    @Slot(pd.DataFrame, pd.DataFrame)
    def update_plots(self, input_parts, other_parts):
        parameters = list(set(input_parts["name"]))

        # Precompute timestamps
        input_parts['created_at_numeric'] = input_parts['created_at'].apply(lambda x: x.timestamp())
        other_parts['created_at_numeric'] = other_parts['created_at'].apply(lambda x: x.timestamp())

        for parameter in parameters:
            other_parts_param = other_parts[other_parts["name"] == parameter]
            input_parts_param = input_parts[input_parts["name"] == parameter]

            # Get the limits for the current parameter
            parameter_limits = input_parts_param.iloc[0][["lower_limit", "upper_limit"]]

            # Calculate distances between each blue point and each red point
            blue_points = other_parts_param[['created_at_numeric', 'value']].to_numpy()

            # Identify outlier red points (those outside the main cluster of blue points)
            blue_value_mean = other_parts_param['value'].mean()
            blue_value_std = other_parts_param['value'].std()
            red_outliers = (input_parts_param['value'] < blue_value_mean - 2 * blue_value_std) | \
                           (input_parts_param['value'] > blue_value_mean + 2 * blue_value_std)
            red_outlier_points = input_parts_param[red_outliers][['created_at_numeric', 'value']].to_numpy()

            # Identify outlier blue points (those outside the main cluster of blue points)
            if len(red_outlier_points) > 0:
                blue_outliers = (other_parts_param['value'] < blue_value_mean - 2 * blue_value_std) | \
                                (other_parts_param['value'] > blue_value_mean + 2 * blue_value_std)

                # Calculate distances from blue points to red outlier points
                distances = distance.cdist(blue_points, red_outlier_points, 'euclidean')

                # Minimum distance for each blue point to any red outlier point
                min_distances = distances.min(axis=1)

                # Determine blue points that are considered close to red outlier points
                threshold_distance = np.percentile(min_distances, 9) if len(min_distances) > 0 else 0
                close_blue_points = min_distances < threshold_distance
            else:
                blue_outliers = np.zeros(len(other_parts_param), dtype=bool)
                close_blue_points = np.zeros(len(other_parts_param), dtype=bool)

            # Create a scatter plot with Plotly
            fig = make_subplots(specs=[[{"secondary_y": True}]])

            # Blue points trace
            fig.add_trace(
                go.Scatter(
                    x=other_parts_param["created_at"],
                    y=other_parts_param["value"],
                    mode="markers",
                    marker=dict(
                        color='blue',
                    ),
                    name="Parts Produced",
                    text=other_parts_param["unit_serial_number"],
                ),
                secondary_y=False,
            )

            # Yellow points trace (outliers)
            if np.any(blue_outliers):
                fig.add_trace(
                    go.Scatter(
                        x=other_parts_param[blue_outliers]["created_at"],
                        y=other_parts_param[blue_outliers]["value"],
                        mode="markers",
                        marker=dict(
                            color='yellow',
                            line=dict(width=1, color='gray')  # Add border to yellow points
                        ),
                        name="Outlier Parts Produced",
                        text=other_parts_param[blue_outliers]["unit_serial_number"],
                    ),
                    secondary_y=False,
                )

            # Red points trace
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

            # Add horizontal lines for the lower and upper limits
            fig.add_trace(
                go.Scatter(
                    x=[other_parts_param["created_at"].min(), other_parts_param["created_at"].max()],
                    y=[parameter_limits["lower_limit"], parameter_limits["lower_limit"]],
                    mode="lines",
                    line=dict(color="navy", width=2, dash="dash"),
                    name="Lower Limit",
                    showlegend=True,  # Ensure the limit appears in the legend
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
                    showlegend=True,  # Ensure the limit appears in the legend
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

            # Create the absolute path of the HTML file
            file_path = os.path.join(os.getcwd(), f"temp_plot_{parameter}.html")

            # Convert the plot to HTML and save it
            fig.write_html(file_path)

            # Create a QWebEngineView
            view = QWebEngineView()
            view.setFixedSize(800, 600)
            # Load the HTML file
            view.load(QUrl.fromLocalFile(file_path))

            # Add the QWebEngineView to the QVBoxLayout
            self.vb_plots.addWidget(view)