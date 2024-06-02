# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advanced_overview_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AdvancedOverviewWidget(object):
    def setupUi(self, AdvancedOverviewWidget):
        if not AdvancedOverviewWidget.objectName():
            AdvancedOverviewWidget.setObjectName(u"AdvancedOverviewWidget")
        AdvancedOverviewWidget.resize(960, 540)
        AdvancedOverviewWidget.setMinimumSize(QSize(960, 540))
        AdvancedOverviewWidget.setStyleSheet(u"QWidget#AdvancedOverviewWidget {\n"
"	background-color: rgb(34, 48, 56);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color: rgb(190, 190, 190);\n"
"	background-color: rgb(55, 79, 91);\n"
"    }\n"
"")
        self.verticalLayout = QVBoxLayout(AdvancedOverviewWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_info = QPushButton(AdvancedOverviewWidget)
        self.pb_info.setObjectName(u"pb_info")

        self.horizontalLayout.addWidget(self.pb_info)

        self.pb_settings = QPushButton(AdvancedOverviewWidget)
        self.pb_settings.setObjectName(u"pb_settings")

        self.horizontalLayout.addWidget(self.pb_settings)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lb_title = QLabel(AdvancedOverviewWidget)
        self.lb_title.setObjectName(u"lb_title")
        font = QFont()
        font.setFamilies([u"Vitesco"])
        font.setPointSize(24)
        font.setBold(True)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet(u"QLabel#lb_title\n"
"{\n"
"color: rgb(190, 190, 190);\n"
"}")

        self.verticalLayout.addWidget(self.lb_title, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_station = QLabel(AdvancedOverviewWidget)
        self.lb_station.setObjectName(u"lb_station")
        font1 = QFont()
        font1.setFamilies([u"Vitesco"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.lb_station.setFont(font1)
        self.lb_station.setStyleSheet(u"QLabel#lb_station\n"
"{\n"
"color: rgb(190, 190, 190);\n"
"}")

        self.horizontalLayout_4.addWidget(self.lb_station)

        self.lb_message = QLabel(AdvancedOverviewWidget)
        self.lb_message.setObjectName(u"lb_message")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(10)
        self.lb_message.setFont(font2)
        self.lb_message.setStyleSheet(u"color: rgb(190, 190, 190);")

        self.horizontalLayout_4.addWidget(self.lb_message)

        self.placeholder_2 = QLabel(AdvancedOverviewWidget)
        self.placeholder_2.setObjectName(u"placeholder_2")

        self.horizontalLayout_4.addWidget(self.placeholder_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sa_radio_buttons = QScrollArea(AdvancedOverviewWidget)
        self.sa_radio_buttons.setObjectName(u"sa_radio_buttons")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sa_radio_buttons.sizePolicy().hasHeightForWidth())
        self.sa_radio_buttons.setSizePolicy(sizePolicy)
        self.sa_radio_buttons.setMinimumSize(QSize(200, 404))
        self.sa_radio_buttons.setMaximumSize(QSize(200, 16777215))
        self.sa_radio_buttons.setStyleSheet(u"QWidget#sa_contents_buttons {\n"
"    background-color: rgb(34, 48, 56);\n"
"    border: 2px solid rgb(80, 118, 70);\n"
"    border-radius: 18px; /* Set the border radius for rounded corners */\n"
"    padding: 5px; /* Add some padding to ensure the contents do not touch the borders */\n"
"    margin: 0; /* Remove any default margin */\n"
"}\n"
"\n"
"QScrollArea {\n"
"	background-color:rgba(0,0,0,0);\n"
"	border: none;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	font: 24pt Vitesco;\n"
"	color: rgb(190, 190, 190);\n"
"    spacing: 12px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 24px;\n"
"    height: 24px;\n"
"	background-color: rgb(190, 190, 190);\n"
"	border-radius: 12px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"   background-color: rgb(80, 118, 70);;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    width: 20px;\n"
"    margin: 10px 10px 10px 0px;  /* top right bottom left */\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"	bac"
                        "kground-color: rgb(44, 62, 72);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"   \n"
"	background-color: rgb(42, 59, 68);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"   background-color: rgb(34, 48, 56)\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    height: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    \n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.sa_radio_buttons.setWidgetResizable(True)
        self.sa_contents_buttons = QWidget()
        self.sa_contents_buttons.setObjectName(u"sa_contents_buttons")
        self.sa_contents_buttons.setGeometry(QRect(0, 0, 200, 404))
        self.sa_radio_buttons.setWidget(self.sa_contents_buttons)

        self.horizontalLayout_2.addWidget(self.sa_radio_buttons)

        self.sa_plots = QScrollArea(AdvancedOverviewWidget)
        self.sa_plots.setObjectName(u"sa_plots")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.sa_plots.sizePolicy().hasHeightForWidth())
        self.sa_plots.setSizePolicy(sizePolicy1)
        self.sa_plots.setStyleSheet(u"QWidget#sa_contents_plots {\n"
"    background-color: rgb(34, 48, 56);\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    border: none;\n"
"}\n"
"\n"
"/* Vertical Scrollbar */\n"
"QScrollBar:vertical {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    width: 20px;\n"
"    margin: 10px 10px 10px 0px;  /* top right bottom left */\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(44, 62, 72);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(42, 59, 68);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: rgb(34, 48, 56);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    height: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background-color: rgb"
                        "a(0, 0, 0, 0);\n"
"}\n"
"\n"
"/* Horizontal Scrollbar */\n"
"QScrollBar:horizontal {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    height: 20px;\n"
"    margin: 0px 10px 10px 10px;  /* top right bottom left */\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(44, 62, 72);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: rgb(42, 59, 68);\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: rgb(34, 48, 56);\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    width: 10px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:horizontal {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"")
        self.sa_plots.setWidgetResizable(True)
        self.sa_contents_plots = QWidget()
        self.sa_contents_plots.setObjectName(u"sa_contents_plots")
        self.sa_contents_plots.setGeometry(QRect(0, 0, 734, 358))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sa_contents_plots.sizePolicy().hasHeightForWidth())
        self.sa_contents_plots.setSizePolicy(sizePolicy2)
        self.sa_contents_plots.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(190, 190, 190);\n"
"}")
        self.vb_plots = QVBoxLayout(self.sa_contents_plots)
        self.vb_plots.setObjectName(u"vb_plots")
        self.vb_plots.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.sa_plots.setWidget(self.sa_contents_plots)

        self.horizontalLayout_2.addWidget(self.sa_plots)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.placeholder = QLabel(AdvancedOverviewWidget)
        self.placeholder.setObjectName(u"placeholder")

        self.horizontalLayout_3.addWidget(self.placeholder, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.pb_overview = QPushButton(AdvancedOverviewWidget)
        self.pb_overview.setObjectName(u"pb_overview")
        font3 = QFont()
        font3.setFamilies([u"Vitesco"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.pb_overview.setFont(font3)
        self.pb_overview.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color: white;\n"
"	background-color: rgb(215,0,75)\n"
"    }")

        self.horizontalLayout_3.addWidget(self.pb_overview, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pb_export = QPushButton(AdvancedOverviewWidget)
        self.pb_export.setObjectName(u"pb_export")
        self.pb_export.setEnabled(False)
        font4 = QFont()
        font4.setBold(True)
        self.pb_export.setFont(font4)
        self.pb_export.setStyleSheet(u"QPushButton:Enabled{\n"
"	background-color: rgb(53, 78, 40);\n"
"	color: rgba(255,255,255, 200);\n"
"}\n"
"QPushButton:Disabled{\n"
"	background-color: rgba(53, 78, 40, 100);\n"
"	color: rgba(255,255,255, 100);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pb_export, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(AdvancedOverviewWidget)

        QMetaObject.connectSlotsByName(AdvancedOverviewWidget)
    # setupUi

    def retranslateUi(self, AdvancedOverviewWidget):
        AdvancedOverviewWidget.setWindowTitle(QCoreApplication.translate("AdvancedOverviewWidget", u"Form", None))
        self.pb_info.setText(QCoreApplication.translate("AdvancedOverviewWidget", u"Info", None))
        self.pb_settings.setText(QCoreApplication.translate("AdvancedOverviewWidget", u"Settings", None))
        self.lb_title.setText(QCoreApplication.translate("AdvancedOverviewWidget", u"Advanced Overview", None))
        self.lb_station.setText(QCoreApplication.translate("AdvancedOverviewWidget", u"Station", None))
        self.lb_message.setText("")
        self.placeholder_2.setText("")
        self.placeholder.setText("")
        self.pb_overview.setText(QCoreApplication.translate("AdvancedOverviewWidget", u"Go to Overview", None))
        self.pb_export.setText(QCoreApplication.translate("AdvancedOverviewWidget", u"Export data", None))
    # retranslateUi

