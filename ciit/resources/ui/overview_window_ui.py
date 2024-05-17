# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'overview_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_OverviewWidget(object):
    def setupUi(self, OverviewWidget):
        if not OverviewWidget.objectName():
            OverviewWidget.setObjectName(u"OverviewWidget")
        OverviewWidget.resize(960, 540)
        OverviewWidget.setMinimumSize(QSize(960, 540))
        OverviewWidget.setStyleSheet(u"QWidget#OverviewWidget {\n"
"background-color: rgb(34, 48, 56);\n"
"}")
        self.verticalLayout = QVBoxLayout(OverviewWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_title = QLabel(OverviewWidget)
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

        self.lb_station = QLabel(OverviewWidget)
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

        self.verticalLayout.addWidget(self.lb_station, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.sa_radio_buttons = QScrollArea(OverviewWidget)
        self.sa_radio_buttons.setObjectName(u"sa_radio_buttons")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sa_radio_buttons.sizePolicy().hasHeightForWidth())
        self.sa_radio_buttons.setSizePolicy(sizePolicy)
        self.sa_radio_buttons.setMinimumSize(QSize(311, 408))
        self.sa_radio_buttons.setMaximumSize(QSize(400, 16777215))
        self.sa_radio_buttons.setStyleSheet(u"QWidget#sa_contents_buttons {\n"
"background-color: rgb(34, 48, 56);\n"
"}\n"
"QRadioButton {\n"
"	font: 20pt Vitesco;\n"
"	color: rgb(190, 190, 190);\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 20px;\n"
"    height: 20px;\n"
"	background-color: rgb(190, 190, 190);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"   background-color: #F0E614;\n"
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
"	background-color: rgb(44, 62, 72);\n"
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
"    background-color: rgba(0, "
                        "0, 0, 0);\n"
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
        self.sa_contents_buttons.setGeometry(QRect(0, 0, 309, 406))
        self.sa_radio_buttons.setWidget(self.sa_contents_buttons)

        self.horizontalLayout_2.addWidget(self.sa_radio_buttons)

        self.tw_params = QTableWidget(OverviewWidget)
        self.tw_params.setObjectName(u"tw_params")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tw_params.sizePolicy().hasHeightForWidth())
        self.tw_params.setSizePolicy(sizePolicy1)
        self.tw_params.setMinimumSize(QSize(0, 408))
        font2 = QFont()
        font2.setFamilies([u"Vitesco"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.tw_params.setFont(font2)
        self.tw_params.setStyleSheet(u"QTableWidget {\n"
"    gridline-color: #606060;\n"
"    background-color: #404040;\n"
"    background-color: rgb(34, 48, 56);\n"
"    border: none;\n"
"	font: 12pt \"Vitesco\";\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 5px;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: #808080;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #303030;\n"
"    color: #E0E0E0;\n"
"    padding: 5px;\n"
"    border: 1px solid #606060;\n"
"	font: 12pt \"Vitesco\";\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"    background-color: #303030;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
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
"    "
                        "border-radius: 5px;\n"
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
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::add-page:horizontal,\n"
"QScrollBar::sub-page:vertical, QScrollBar::sub-page:horizontal {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.tw_params.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.horizontalLayout_2.addWidget(self.tw_params)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pb_advanced_overview = QPushButton(OverviewWidget)
        self.pb_advanced_overview.setObjectName(u"pb_advanced_overview")
        font3 = QFont()
        font3.setFamilies([u"Vitesco"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.pb_advanced_overview.setFont(font3)
        self.pb_advanced_overview.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color: white;\n"
"	background-color: rgb(215,0,75)\n"
"    }")

        self.verticalLayout.addWidget(self.pb_advanced_overview, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(OverviewWidget)

        QMetaObject.connectSlotsByName(OverviewWidget)
    # setupUi

    def retranslateUi(self, OverviewWidget):
        OverviewWidget.setWindowTitle(QCoreApplication.translate("OverviewWidget", u"Form", None))
        self.lb_title.setText(QCoreApplication.translate("OverviewWidget", u"Overview", None))
        self.lb_station.setText(QCoreApplication.translate("OverviewWidget", u"Station", None))
        self.pb_advanced_overview.setText(QCoreApplication.translate("OverviewWidget", u"Go to Advanced Overview", None))
    # retranslateUi

