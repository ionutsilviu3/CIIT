# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)
import resources.icons.icons_rc

class Ui_info_window(object):
    def setupUi(self, info_window):
        if not info_window.objectName():
            info_window.setObjectName(u"info_window")
        info_window.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(info_window.sizePolicy().hasHeightForWidth())
        info_window.setSizePolicy(sizePolicy)
        info_window.setMinimumSize(QSize(960, 540))
        info_window.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        info_window.setFont(font)
        info_window.setStyleSheet(u"QPushButton {\n"
"	border-radius: 16px;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color: rgb(190, 190, 190);\n"
"	background-color: rgb(55, 79, 91);\n"
"    }\n"
"\n"
"QWidget {\n"
" background-color: rgb(34, 48, 56);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(info_window)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.pb_contacts = QPushButton(info_window)
        self.pb_contacts.setObjectName(u"pb_contacts")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.pb_contacts.setFont(font1)
        self.pb_contacts.setStyleSheet(u"QPushButton {\n"
"	border-radius: 16px;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color:rgb(226, 220, 220);\n"
"	background-color: rgb(56, 76, 83);\n"
"    }")
        icon = QIcon()
        icon.addFile(u":/Icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_contacts.setIcon(icon)
        self.pb_contacts.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pb_contacts, 1, 2, 1, 1)

        self.lb_title = QLabel(info_window)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Vitesco"])
        font2.setPointSize(32)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.lb_title.setFont(font2)
        self.lb_title.setStyleSheet(u"QLabel\n"
"{\n"
"    color: rgb(226, 220, 220);\n"
"}")
        self.lb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_title, 1, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pb_back = QPushButton(info_window)
        self.pb_back.setObjectName(u"pb_back")
        self.pb_back.setFont(font1)
        self.pb_back.setStyleSheet(u"QPushButton {\n"
"	border-radius: 16px;\n"
"	padding-left: 8px;\n"
"	padding-right: 8px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color:rgb(226, 220, 220);\n"
"	background-color: rgb(56, 76, 83);\n"
"    }")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_back.setIcon(icon1)
        self.pb_back.setIconSize(QSize(24, 24))

        self.gridLayout.addWidget(self.pb_back, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_previous_page = QPushButton(info_window)
        self.pb_previous_page.setObjectName(u"pb_previous_page")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(24)
        font3.setBold(False)
        self.pb_previous_page.setFont(font3)
        self.pb_previous_page.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(34, 48, 56, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 43, 50);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(24, 35, 40)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_previous_page.setIcon(icon2)
        self.pb_previous_page.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.pb_previous_page)

        self.sw_pages = QStackedWidget(info_window)
        self.sw_pages.setObjectName(u"sw_pages")
        self.sw_pages.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"image: url(:/Info/info1.png);\n"
"")
        self.sw_pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"image: url(:/Images/overview.png);")
        self.sw_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"image: url(:/Images/advanced.png);")
        self.verticalLayout_2 = QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sw_pages.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.sw_pages)

        self.pb_next_page = QPushButton(info_window)
        self.pb_next_page.setObjectName(u"pb_next_page")
        self.pb_next_page.setFont(font3)
        self.pb_next_page.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(34, 48, 56, 255);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 43, 50);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(24, 35, 40)\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_next_page.setIcon(icon3)
        self.pb_next_page.setIconSize(QSize(48, 48))

        self.horizontalLayout.addWidget(self.pb_next_page)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)


        self.retranslateUi(info_window)

        self.sw_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(info_window)
    # setupUi

    def retranslateUi(self, info_window):
        info_window.setWindowTitle(QCoreApplication.translate("info_window", u"CIIT", None))
        self.pb_contacts.setText(QCoreApplication.translate("info_window", u"Contacts", None))
        self.lb_title.setText(QCoreApplication.translate("info_window", u"Info", None))
        self.pb_back.setText(QCoreApplication.translate("info_window", u"Go Back", None))
        self.pb_previous_page.setText("")
        self.pb_next_page.setText("")
    # retranslateUi

