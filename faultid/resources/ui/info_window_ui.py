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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
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
        self.verticalLayout = QVBoxLayout(info_window)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_back = QPushButton(info_window)
        self.pb_back.setObjectName(u"pb_back")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.pb_back.setFont(font1)
        self.pb_back.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 8px;\n"
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
        icon.addFile(u":/Icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_back.setIcon(icon)
        self.pb_back.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pb_back, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.pb_contacts = QPushButton(info_window)
        self.pb_contacts.setObjectName(u"pb_contacts")
        self.pb_contacts.setFont(font1)
        self.pb_contacts.setStyleSheet(u"QPushButton {\n"
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
        icon1.addFile(u":/Icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_contacts.setIcon(icon1)
        self.pb_contacts.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pb_contacts, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.lb_title = QLabel(info_window)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.lb_title.setFont(font2)
        self.lb_title.setStyleSheet(u"QLabel\n"
"{\n"
"    color: rgb(226, 220, 220);\n"
"}")
        self.lb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.lb_title, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.placeholder_left = QLabel(info_window)
        self.placeholder_left.setObjectName(u"placeholder_left")
        self.placeholder_left.setMinimumSize(QSize(60, 10))
        self.placeholder_left.setMaximumSize(QSize(180, 10))

        self.horizontalLayout.addWidget(self.placeholder_left)

        self.pb_previous_page = QPushButton(info_window)
        self.pb_previous_page.setObjectName(u"pb_previous_page")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(24)
        font3.setBold(False)
        self.pb_previous_page.setFont(font3)
        self.pb_previous_page.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(34, 48, 56);\n"
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

        self.horizontalLayout.addWidget(self.pb_previous_page, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.sw_pages = QStackedWidget(info_window)
        self.sw_pages.setObjectName(u"sw_pages")
        self.sw_pages.setMinimumSize(QSize(600, 400))
        self.sw_pages.setMaximumSize(QSize(1200, 800))
        self.sw_pages.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"image: url(:/Info/info1.png);")
        self.sw_pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"image: url(:/Info/info2.png);")
        self.sw_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"image: url(:/Info/info3.png);")
        self.verticalLayout_2 = QVBoxLayout(self.page_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.sw_pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"image: url(:/Info/info4.png);")
        self.sw_pages.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"image: url(:/Info/info5.png);")
        self.sw_pages.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"image: url(:/Info/info6.png);")
        self.sw_pages.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.page_7.setStyleSheet(u"image: url(:/Info/info7.png);")
        self.sw_pages.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.page_8.setStyleSheet(u"image: url(:/Info/info8.png);")
        self.sw_pages.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setStyleSheet(u"image: url(:/Info/info9.png);")
        self.sw_pages.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.page_10.setStyleSheet(u"image: url(:/Info/info10.png);")
        self.sw_pages.addWidget(self.page_10)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.page_11.setStyleSheet(u"image: url(:/Info/info11.png);")
        self.sw_pages.addWidget(self.page_11)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.page_12.setStyleSheet(u"image: url(:/Info/info12.png);")
        self.sw_pages.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.page_13.setStyleSheet(u"image: url(:/Info/info13.png);")
        self.sw_pages.addWidget(self.page_13)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.page_14.setStyleSheet(u"image: url(:/Info/info14.png);")
        self.sw_pages.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.page_15.setStyleSheet(u"image: url(:/Info/info15.png);")
        self.sw_pages.addWidget(self.page_15)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.page_16.setStyleSheet(u"image: url(:/Info/info16.png);")
        self.sw_pages.addWidget(self.page_16)

        self.horizontalLayout.addWidget(self.sw_pages)

        self.pb_next_page = QPushButton(info_window)
        self.pb_next_page.setObjectName(u"pb_next_page")
        self.pb_next_page.setFont(font3)
        self.pb_next_page.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(34, 48, 56);\n"
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

        self.horizontalLayout.addWidget(self.pb_next_page, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.placeholder_right = QLabel(info_window)
        self.placeholder_right.setObjectName(u"placeholder_right")
        self.placeholder_right.setMinimumSize(QSize(60, 10))
        self.placeholder_right.setMaximumSize(QSize(180, 10))

        self.horizontalLayout.addWidget(self.placeholder_right)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(info_window)

        self.sw_pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(info_window)
    # setupUi

    def retranslateUi(self, info_window):
        info_window.setWindowTitle(QCoreApplication.translate("info_window", u"CIIT", None))
        self.pb_back.setText(QCoreApplication.translate("info_window", u"Go Back", None))
        self.pb_contacts.setText(QCoreApplication.translate("info_window", u" Contacts", None))
        self.lb_title.setText(QCoreApplication.translate("info_window", u"Info", None))
        self.placeholder_left.setText("")
        self.pb_previous_page.setText("")
        self.pb_next_page.setText("")
        self.placeholder_right.setText("")
    # retranslateUi

