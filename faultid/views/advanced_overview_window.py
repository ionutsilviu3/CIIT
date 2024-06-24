import os
from pathlib import Path
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Slot, Signal, QDir
from PySide6.QtWidgets import QWidget, QVBoxLayout, QRadioButton, QFileDialog, QSizePolicy
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np

from resources.ui.advanced_overview_window_ui import Ui_AdvancedOverviewWidget

class AdvancedOverviewWindow(QWidget, Ui_AdvancedOverviewWidget):
    # Define signals for inter-object communication
    radio_button_clicked_signal = Signal()
    go_to_overview_signal = Signal()
    go_to_settings_signal = Signal()
    export_data_signal = Signal()
    go_to_info_signal = Signal()
    
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)  # Set up the UI defined in Ui_AdvancedOverviewWidget
        self.app = app  # Store the application instance
        self.vb_locations = QVBoxLayout()  # Vertical layout for radio buttons
        self.vb_locations.setSpacing(16)  # Set spacing between radio buttons
        self.vb_plots.setSpacing(16)  # Set spacing between plot views
        self.sa_contents_buttons.setLayout(self.vb_locations)  # Set layout for radio buttons container
        self.sa_radio_buttons.setWidget(self.sa_contents_buttons)  # Set widget for scroll area
        # Connect buttons to corresponding signals
        self.pb_overview.clicked.connect(self.go_to_overview_signal.emit)
        self.pb_settings.clicked.connect(self.go_to_settings_signal)
        self.pb_export.clicked.connect(self.export_data_signal)
        self.pb_info.clicked.connect(self.go_to_info_signal)
        self.views = {}  # Dictionary to store views (not currently used)
        self.selected_location = None  # Store currently selected location
        self.locations_radio_buttons = []  # List to store radio buttons
        self.cleanup_html_files()
        
    def cleanup_html_files(self):
        """
        Removes all HTML files in the temp directory.
        """
        try:
            project_directory = Path(__file__).resolve().parents[1]
            temp_folder_path = project_directory / 'temp'
            
            # Ensure temp folder exists before attempting to clean up
            if temp_folder_path.exists() and temp_folder_path.is_dir():
                html_files = temp_folder_path.glob("*.html")
                for file in html_files:
                    file.unlink()
            else:
                print("Temp directory does not exist or is not accessible.")
                    
        except Exception as e:
            print(f"Error while cleaning up HTML files: {e}")
        
    @Slot()
    def get_selected_location(self):
        """Returns the text of the selected radio button."""
        for radio_button in self.locations_radio_buttons:
            if radio_button.isChecked():
                self.selected_location = radio_button.text()
                return self.selected_location

    @Slot()
    def update_radio_buttons(self, locations):
        """Updates radio buttons based on the provided locations."""
        for loc in locations:
            radio_button = QRadioButton(loc)
            radio_button.clicked.connect(self.radio_button_clicked_signal)
            self.vb_locations.addWidget(radio_button)
            self.locations_radio_buttons.append(radio_button)
    
    def clear_plots(self):
        """Clears existing plot views."""
        while self.vb_plots.count():
            item = self.vb_plots.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()  # Delete the widget and free up resources
    
    def create_plot(self, parameter, other_parts_param, input_parts_param, blue_outliers, parameter_limits):
        """Creates a scatter plot using Plotly and displays it in a QWebEngineView."""
        fig = make_subplots(specs=[[{"secondary_y": True}]])  # Initialize subplot
        
        # Add trace for parts produced
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
        
        # Add trace for outlier parts produced if any exist
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
        
        # Add trace for input parts
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
        
        # Add horizontal lines for parameter limits
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
        
        # Update layout of the plot
        fig.update_layout(
            title_text=f"Scatter Plot of {parameter} Value Over Time",
            xaxis_title="Time (days since start)",
            yaxis_title="Parameter Value",
            legend_title="Legend",
            legend=dict(itemsizing='constant'),
        )
        
        # Write the plot to an HTML file in the temp folder
        file_name = f"temp_plot_{parameter}.html"
        temp_folder_path = os.path.join(os.getcwd(), 'faultid', 'temp')

        if not os.path.exists(temp_folder_path):
            os.makedirs(temp_folder_path)

        file_path = os.path.join(temp_folder_path, file_name)

        # Save the plot to the new path
        fig.write_html(file_path)
        
        # Display the plot in a QWebEngineView
        view = QWebEngineView()
        
        view.load(QUrl.fromLocalFile(file_path))  # Load HTML file into the view
        
        # Set minimum size constraints
        view.setMinimumSize(700, 450)
        view.setMaximumWidth(1200)
        
        # Set size policy to allow expansion
        size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        view.setSizePolicy(size_policy)
        
        # Add the view widget to the layout with a fixed height
        self.vb_plots.addWidget(view)
    
    def get_export_path(self):
        """Opens a file dialog to get the export path for Excel data."""
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
