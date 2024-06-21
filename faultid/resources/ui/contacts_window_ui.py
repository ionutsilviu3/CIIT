# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contacts_window.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources.icons.icons_rc

class Ui_contacts_window(object):
    def setupUi(self, contacts_window):
        if not contacts_window.objectName():
            contacts_window.setObjectName(u"contacts_window")
        contacts_window.resize(960, 541)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(contacts_window.sizePolicy().hasHeightForWidth())
        contacts_window.setSizePolicy(sizePolicy)
        contacts_window.setMinimumSize(QSize(960, 540))
        contacts_window.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(12)
        contacts_window.setFont(font)
        contacts_window.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color: rgb(190, 190, 190);\n"
"	background-color: rgb(55, 79, 91);\n"
"    }\n"
"QWidget#contacts_window{\n"
"background-color: rgb(34, 48, 56);\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(contacts_window)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_back = QPushButton(contacts_window)
        self.pb_back.setObjectName(u"pb_back")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(10)
        font1.setBold(True)
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
        icon = QIcon()
        icon.addFile(u":/Icons/arrow-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_back.setIcon(icon)
        self.pb_back.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_back, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.lb_title = QLabel(contacts_window)
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

        self.horizontalLayout.addWidget(self.lb_title, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.lb_placeholder = QLabel(contacts_window)
        self.lb_placeholder.setObjectName(u"lb_placeholder")
        self.lb_placeholder.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lb_placeholder.sizePolicy().hasHeightForWidth())
        self.lb_placeholder.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.lb_placeholder)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(contacts_window)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"color:rgb(226, 220, 220);\n"
"padding-left: 8px;")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_email = QLabel(contacts_window)
        self.lb_email.setObjectName(u"lb_email")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(16)
        self.lb_email.setFont(font4)
        self.lb_email.setStyleSheet(u"color: rgb(226, 220, 220);")

        self.gridLayout.addWidget(self.lb_email, 1, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.lb_image_phone = QLabel(contacts_window)
        self.lb_image_phone.setObjectName(u"lb_image_phone")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_image_phone.sizePolicy().hasHeightForWidth())
        self.lb_image_phone.setSizePolicy(sizePolicy2)
        self.lb_image_phone.setFont(font4)
        self.lb_image_phone.setStyleSheet(u"color: rgb(226, 220, 220); padding-left: 8px;")
        self.lb_image_phone.setPixmap(QPixmap(u":/Icons/phone.svg"))

        self.gridLayout.addWidget(self.lb_image_phone, 2, 0, 1, 1)

        self.lb_phone = QLabel(contacts_window)
        self.lb_phone.setObjectName(u"lb_phone")
        self.lb_phone.setFont(font4)
        self.lb_phone.setStyleSheet(u"color: rgb(226, 220, 220);")

        self.gridLayout.addWidget(self.lb_phone, 2, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.lb_image_email = QLabel(contacts_window)
        self.lb_image_email.setObjectName(u"lb_image_email")
        sizePolicy2.setHeightForWidth(self.lb_image_email.sizePolicy().hasHeightForWidth())
        self.lb_image_email.setSizePolicy(sizePolicy2)
        self.lb_image_email.setFont(font4)
        self.lb_image_email.setStyleSheet(u"color: rgb(226, 220, 220); padding-left: 8px;")
        self.lb_image_email.setPixmap(QPixmap(u":/Icons/mail.svg"))

        self.gridLayout.addWidget(self.lb_image_email, 1, 0, 1, 1)

        self.lb_image_location = QLabel(contacts_window)
        self.lb_image_location.setObjectName(u"lb_image_location")
        sizePolicy2.setHeightForWidth(self.lb_image_location.sizePolicy().hasHeightForWidth())
        self.lb_image_location.setSizePolicy(sizePolicy2)
        self.lb_image_location.setFont(font4)
        self.lb_image_location.setStyleSheet(u"color: rgb(226, 220, 220); padding-left: 8px;")
        self.lb_image_location.setPixmap(QPixmap(u":/Icons/map-pin.svg"))

        self.gridLayout.addWidget(self.lb_image_location, 3, 0, 1, 1)

        self.lb_location = QLabel(contacts_window)
        self.lb_location.setObjectName(u"lb_location")
        self.lb_location.setFont(font4)
        self.lb_location.setStyleSheet(u"color: rgb(226, 220, 220);")

        self.gridLayout.addWidget(self.lb_location, 3, 1, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.lb_image = QLabel(contacts_window)
        self.lb_image.setObjectName(u"lb_image")
        sizePolicy1.setHeightForWidth(self.lb_image.sizePolicy().hasHeightForWidth())
        self.lb_image.setSizePolicy(sizePolicy1)
        self.lb_image.setMinimumSize(QSize(256, 256))
        self.lb_image.setMaximumSize(QSize(400, 400))
        self.lb_image.setStyleSheet(u"image: url(:/Images/contacts.png);")

        self.horizontalLayout_2.addWidget(self.lb_image)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(contacts_window)

        QMetaObject.connectSlotsByName(contacts_window)
    # setupUi

    def retranslateUi(self, contacts_window):
        contacts_window.setWindowTitle(QCoreApplication.translate("contacts_window", u"CIIT", None))
        self.pb_back.setText(QCoreApplication.translate("contacts_window", u"Go Back", None))
        self.lb_title.setText(QCoreApplication.translate("contacts_window", u"Contacts", None))
        self.lb_placeholder.setText("")
        self.label.setText(QCoreApplication.translate("contacts_window", u"<html><head/><body><p><span style=\" color:#e2dcdc;\">Get in touch with us if you're feeling </span><span style=\" color:#408264;\">lost</span></p></body></html>", None))
        self.lb_email.setText(QCoreApplication.translate("contacts_window", u"boancionut@gmail.com", None))
        self.lb_image_phone.setText("")
        self.lb_phone.setText(QCoreApplication.translate("contacts_window", u"+40755350594", None))
        self.lb_image_email.setText("")
        self.lb_image_location.setText("")
        self.lb_location.setText(QCoreApplication.translate("contacts_window", u"Brasov, Prejmer, Str. Bisericii, Nr. 111", None))
        self.lb_image.setText("")
    # retranslateUi

