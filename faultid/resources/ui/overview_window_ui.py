# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overview_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import resources.icons.icons_rc

class Ui_OverviewWidget(object):
    def setupUi(self, OverviewWidget):
        if not OverviewWidget.objectName():
            OverviewWidget.setObjectName(u"OverviewWidget")
        OverviewWidget.resize(960, 540)
        OverviewWidget.setMinimumSize(QSize(960, 540))
        OverviewWidget.setStyleSheet(u"QWidget#OverviewWidget {\n"
"background-color: rgb(34, 48, 56);\n"
"}\n"
"\n"
"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color:rgb(226, 220, 220);\n"
"	background-color:#384C53;\n"
"    }")
        self.verticalLayout = QVBoxLayout(OverviewWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pb_settings = QPushButton(OverviewWidget)
        self.pb_settings.setObjectName(u"pb_settings")
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(10)
        font.setBold(True)
        self.pb_settings.setFont(font)
        self.pb_settings.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color: rgb(226, 220, 220);\n"
"	background-color: rgb(56, 76, 83);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 68, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(45, 61, 66);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_settings.setIcon(icon)
        self.pb_settings.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_settings)

        self.pb_info = QPushButton(OverviewWidget)
        self.pb_info.setObjectName(u"pb_info")
        self.pb_info.setFont(font)
        self.pb_info.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color: rgb(226, 220, 220);\n"
"	background-color: rgb(56, 76, 83);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(50, 68, 74);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(45, 61, 66);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_info.setIcon(icon1)
        self.pb_info.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_info)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lb_title = QLabel(OverviewWidget)
        self.lb_title.setObjectName(u"lb_title")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.lb_title.setFont(font1)
        self.lb_title.setStyleSheet(u"QLabel#lb_title\n"
"{\n"
"color: rgb(226, 220, 220);\n"
"}")

        self.verticalLayout.addWidget(self.lb_title, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_station = QLabel(OverviewWidget)
        self.lb_station.setObjectName(u"lb_station")
        font2 = QFont()
        font2.setFamilies([u"Vitesco"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.lb_station.setFont(font2)
        self.lb_station.setStyleSheet(u"QLabel#lb_station\n"
"{\n"
"color: rgb(226, 220, 220);\n"
"}")

        self.horizontalLayout_4.addWidget(self.lb_station)

        self.lb_message = QLabel(OverviewWidget)
        self.lb_message.setObjectName(u"lb_message")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.lb_message.setFont(font3)
        self.lb_message.setStyleSheet(u"QLabel {\n"
"    color: rgb(226, 220, 220);\n"
"    font: 12pt \"Roboto\";\n"
"}")

        self.horizontalLayout_4.addWidget(self.lb_message)

        self.placeholder_2 = QLabel(OverviewWidget)
        self.placeholder_2.setObjectName(u"placeholder_2")

        self.horizontalLayout_4.addWidget(self.placeholder_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sa_radio_buttons = QScrollArea(OverviewWidget)
        self.sa_radio_buttons.setObjectName(u"sa_radio_buttons")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sa_radio_buttons.sizePolicy().hasHeightForWidth())
        self.sa_radio_buttons.setSizePolicy(sizePolicy)
        self.sa_radio_buttons.setMinimumSize(QSize(200, 300))
        self.sa_radio_buttons.setMaximumSize(QSize(200, 16777215))
        self.sa_radio_buttons.setStyleSheet(u"QWidget#sa_contents_buttons {\n"
"    background-color: rgb(34, 48, 56);\n"
"    border: 2px solid rgb(64, 130, 100);\n"
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
"	font: 24pt Roboto;\n"
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
"   background-color: rgb(64, 130, 100);\n"
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
        self.sa_contents_buttons.setGeometry(QRect(0, 0, 200, 339))
        self.sa_contents_buttons.setStyleSheet(u"QWidget > QRadioButton{\n"
"padding-left: 12px;\n"
"}")
        self.sa_radio_buttons.setWidget(self.sa_contents_buttons)

        self.horizontalLayout_2.addWidget(self.sa_radio_buttons)

        self.placeholder_params = QLabel(OverviewWidget)
        self.placeholder_params.setObjectName(u"placeholder_params")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.placeholder_params.sizePolicy().hasHeightForWidth())
        self.placeholder_params.setSizePolicy(sizePolicy1)
        self.placeholder_params.setMinimumSize(QSize(16, 10))
        self.placeholder_params.setMaximumSize(QSize(32, 10))

        self.horizontalLayout_2.addWidget(self.placeholder_params)

        self.tw_params = QTableWidget(OverviewWidget)
        self.tw_params.setObjectName(u"tw_params")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tw_params.sizePolicy().hasHeightForWidth())
        self.tw_params.setSizePolicy(sizePolicy2)
        self.tw_params.setMinimumSize(QSize(760, 450))
        self.tw_params.setMaximumSize(QSize(1700, 700))
        self.tw_params.setFont(font3)
        self.tw_params.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(34, 48, 56);\n"
"    border: none;\n"
"    font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 12px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #384C53;\n"
"    color: rgb(226, 220, 220);\n"
"    padding: 5px;\n"
"    border: none;\n"
"    font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"/* Add borders only between vertical header items */\n"
"QHeaderView::section:horizontal {\n"
"    border-right: 1px solid rgb(34, 48, 56);\n"
"}\n"
"\n"
"QHeaderView::section:vertical {\n"
"	border-bottom: 1px solid rgb(34, 48, 56);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #384C53;\n"
"    border: none;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #384C53;\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    border-right: 1px solid rgb(34, 48, 56) !important;\n"
"    border-bottom: 1px solid rgb(34, 48, 56) !important;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: rgba(0, 0, 0"
                        ", 0);\n"
"    width: 20px;\n"
"    margin: 10px 10px 10px 0px;  /* top right bottom left */\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    height: 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical, QScrollBar::handle:horizontal {\n"
"    background-color: rgb(44, 62, 72);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover, QScrollBar::handle:horizontal:hover {\n"
"    background-color: rgb(42, 59, 68);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed, QScrollBar::handle:horizontal:pressed {\n"
"    background-color: rgb(34, 48, 56);\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    height: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    width: 10px;\n"
"    subcontrol-positio"
                        "n: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:vertical, QScrollBar::sub-page:horizontal {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.tw_params.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tw_params.setAlternatingRowColors(False)
        self.tw_params.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tw_params.setShowGrid(True)
        self.tw_params.setGridStyle(Qt.PenStyle.SolidLine)
        self.tw_params.setCornerButtonEnabled(True)
        self.tw_params.horizontalHeader().setProperty("showSortIndicator", False)

        self.horizontalLayout_2.addWidget(self.tw_params)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.placeholder_left = QLabel(OverviewWidget)
        self.placeholder_left.setObjectName(u"placeholder_left")
        self.placeholder_left.setMinimumSize(QSize(10, 40))

        self.horizontalLayout_3.addWidget(self.placeholder_left, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.pb_advanced_overview = QPushButton(OverviewWidget)
        self.pb_advanced_overview.setObjectName(u"pb_advanced_overview")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        font4.setKerning(True)
        self.pb_advanced_overview.setFont(font4)
        self.pb_advanced_overview.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color: rgb(226, 220, 220);\n"
"	background-color: rgb(64, 130, 100);\n"
"    }\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background-color: rgb(50, 102, 78);\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: rgb(42, 85, 65);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pb_advanced_overview, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.placeholder_right = QLabel(OverviewWidget)
        self.placeholder_right.setObjectName(u"placeholder_right")

        self.horizontalLayout_3.addWidget(self.placeholder_right, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(OverviewWidget)

        QMetaObject.connectSlotsByName(OverviewWidget)
    # setupUi

    def retranslateUi(self, OverviewWidget):
        OverviewWidget.setWindowTitle(QCoreApplication.translate("OverviewWidget", u"Form", None))
        self.pb_settings.setText(QCoreApplication.translate("OverviewWidget", u" Settings", None))
        self.pb_info.setText(QCoreApplication.translate("OverviewWidget", u" Info", None))
        self.lb_title.setText(QCoreApplication.translate("OverviewWidget", u"Overview", None))
        self.lb_station.setText(QCoreApplication.translate("OverviewWidget", u"Station", None))
        self.lb_message.setText("")
        self.placeholder_2.setText("")
        self.placeholder_params.setText("")
        self.placeholder_left.setText("")
        self.pb_advanced_overview.setText(QCoreApplication.translate("OverviewWidget", u"Go to Advanced Overview", None))
        self.placeholder_right.setText("")
    # retranslateUi

