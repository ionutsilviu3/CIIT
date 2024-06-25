# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources.icons.icons_rc

class Ui_Parent(object):
    def setupUi(self, Parent):
        if not Parent.objectName():
            Parent.setObjectName(u"Parent")
        Parent.resize(960, 540)
        Parent.setMinimumSize(QSize(960, 540))
        font = QFont()
        font.setPointSize(12)
        Parent.setFont(font)
        Parent.setStyleSheet(u"QWidget#Parent {background-color: rgb(34, 48, 56)}\n"
"")
        self.horizontalLayout = QHBoxLayout(Parent)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setContentsMargins(26, 26, 26, 26)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, 8, 8, 8)
        self.lb_background = QLabel(Parent)
        self.lb_background.setObjectName(u"lb_background")
        self.lb_background.setMinimumSize(QSize(480, 0))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(8)
        self.lb_background.setFont(font1)
        self.lb_background.setStyleSheet(u"border-image: url(:/Images/vertical_background.jpg);")

        self.horizontalLayout.addWidget(self.lb_background)

        self.Form = QWidget(Parent)
        self.Form.setObjectName(u"Form")
        self.Form.setMinimumSize(QSize(480, 0))
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(16)
        self.Form.setFont(font2)
        self.Form.setStyleSheet(u"QPushButton {\n"
"border-radius: 16px;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.Form)
        self.verticalLayout_3.setSpacing(16)
        self.verticalLayout_3.setContentsMargins(26, 26, 26, 26)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.pb_info = QPushButton(self.Form)
        self.pb_info.setObjectName(u"pb_info")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.pb_info.setFont(font3)
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
        icon = QIcon()
        icon.addFile(u":/Icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_info.setIcon(icon)
        self.pb_info.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.pb_info, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        self.lb_login_title = QLabel(self.Form)
        self.lb_login_title.setObjectName(u"lb_login_title")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(26)
        font4.setBold(True)
        self.lb_login_title.setFont(font4)
        self.lb_login_title.setStyleSheet(u"color: rgb(226, 220, 220);")
        self.lb_login_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lb_login_title, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget = QWidget(self.Form)
        self.widget.setObjectName(u"widget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setFont(font2)
        self.widget.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 16px;	\n"
"	background-color: rgba(29, 38, 30,0);	\n"
"	color: rgb(226, 220, 220);\n"
"	border-style: solid;\n"
"    border-width: 1.5px;\n"
"	border-color: rgb(64, 130, 100);\n"
"}\n"
"")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setSpacing(12)
        self.formLayout.setContentsMargins(26, 26, 26, 26)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setHorizontalSpacing(8)
        self.formLayout.setVerticalSpacing(16)
        self.formLayout.setContentsMargins(8, 8, 8, 8)
        self.lb_user = QLabel(self.widget)
        self.lb_user.setObjectName(u"lb_user")
        self.lb_user.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_user.sizePolicy().hasHeightForWidth())
        self.lb_user.setSizePolicy(sizePolicy1)
        self.lb_user.setMinimumSize(QSize(16, 16))
        self.lb_user.setFont(font2)
        self.lb_user.setPixmap(QPixmap(u":/Icons/mail.svg"))
        self.lb_user.setScaledContents(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lb_user)

        self.le_user = QLineEdit(self.widget)
        self.le_user.setObjectName(u"le_user")
        sizePolicy1.setHeightForWidth(self.le_user.sizePolicy().hasHeightForWidth())
        self.le_user.setSizePolicy(sizePolicy1)
        self.le_user.setMinimumSize(QSize(256, 48))
        self.le_user.setMaximumSize(QSize(256, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(12)
        self.le_user.setFont(font5)
        self.le_user.setToolTipDuration(-1)
        self.le_user.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.le_user.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_user)

        self.lb_password = QLabel(self.widget)
        self.lb_password.setObjectName(u"lb_password")
        self.lb_password.setPixmap(QPixmap(u":/Icons/lock.svg"))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lb_password)

        self.le_password = QLineEdit(self.widget)
        self.le_password.setObjectName(u"le_password")
        sizePolicy1.setHeightForWidth(self.le_password.sizePolicy().hasHeightForWidth())
        self.le_password.setSizePolicy(sizePolicy1)
        self.le_password.setMinimumSize(QSize(256, 48))
        self.le_password.setMaximumSize(QSize(192, 16777215))
        self.le_password.setFont(font5)
        self.le_password.setToolTipDuration(-1)
        self.le_password.setEchoMode(QLineEdit.EchoMode.Password)
        self.le_password.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.le_password.setClearButtonEnabled(False)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.le_password)

        self.lb_warning_icon = QLabel(self.widget)
        self.lb_warning_icon.setObjectName(u"lb_warning_icon")
        self.lb_warning_icon.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.lb_warning_icon.sizePolicy().hasHeightForWidth())
        self.lb_warning_icon.setSizePolicy(sizePolicy1)
        self.lb_warning_icon.setMinimumSize(QSize(32, 32))
        font6 = QFont()
        font6.setFamilies([u"Roboto"])
        font6.setPointSize(16)
        font6.setBold(False)
        self.lb_warning_icon.setFont(font6)
        self.lb_warning_icon.setStyleSheet(u"QLabel#lb_warning_icon:disabled\n"
"{\n"
"	border-image: none;\n"
"}\n"
"\n"
"QLabel#lb_warning_icon:enabled\n"
"{\n"
"	\n"
"	border-image: url(:/Icons/alert-circle.svg);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.lb_warning_icon)

        self.lb_warning_message = QLabel(self.widget)
        self.lb_warning_message.setObjectName(u"lb_warning_message")
        self.lb_warning_message.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_warning_message.sizePolicy().hasHeightForWidth())
        self.lb_warning_message.setSizePolicy(sizePolicy2)
        self.lb_warning_message.setMinimumSize(QSize(256, 40))
        self.lb_warning_message.setMaximumSize(QSize(256, 40))
        font7 = QFont()
        font7.setFamilies([u"Roboto"])
        font7.setPointSize(12)
        font7.setBold(True)
        self.lb_warning_message.setFont(font7)
        self.lb_warning_message.setStyleSheet(u"QLabel\n"
"{\n"
"color: rgb(138, 29, 0);\n"
"}\n"
"QLabel:disabled\n"
"{\n"
"	color: rgba(0, 0, 0, 0);\n"
"}")
        self.lb_warning_message.setFrameShape(QFrame.Shape.NoFrame)
        self.lb_warning_message.setFrameShadow(QFrame.Shadow.Plain)
        self.lb_warning_message.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lb_warning_message.setWordWrap(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lb_warning_message)


        self.verticalLayout_3.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pb_log_in = QPushButton(self.Form)
        self.pb_log_in.setObjectName(u"pb_log_in")
        sizePolicy1.setHeightForWidth(self.pb_log_in.sizePolicy().hasHeightForWidth())
        self.pb_log_in.setSizePolicy(sizePolicy1)
        self.pb_log_in.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setFamilies([u"Roboto"])
        font8.setPointSize(16)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setUnderline(False)
        font8.setKerning(True)
        self.pb_log_in.setFont(font8)
#if QT_CONFIG(tooltip)
        self.pb_log_in.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.pb_log_in.setToolTipDuration(-1)
        self.pb_log_in.setStyleSheet(u"QPushButton\n"
"{\n"
"background-color: rgb(64, 130, 100);\n"
"color: rgb(226, 220, 220);\n"
"border-radius: 20px;\n"
"padding-left: 24px;\n"
"padding-right: 24px;\n"
"padding-top: 16px;\n"
"padding-bottom: 16px;\n"
"}\n"
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
        icon1 = QIcon()
        icon1.addFile(u":/Icons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_log_in.setIcon(icon1)
        self.pb_log_in.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.pb_log_in, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout.addWidget(self.Form)

        QWidget.setTabOrder(self.pb_log_in, self.le_user)
        QWidget.setTabOrder(self.le_user, self.le_password)

        self.retranslateUi(Parent)

        QMetaObject.connectSlotsByName(Parent)
    # setupUi

    def retranslateUi(self, Parent):
        Parent.setWindowTitle(QCoreApplication.translate("Parent", u"Login", None))
        self.lb_background.setText("")
        self.pb_info.setText(QCoreApplication.translate("Parent", u" Info", None))
        self.lb_login_title.setText(QCoreApplication.translate("Parent", u"Log in", None))
        self.lb_user.setText("")
#if QT_CONFIG(tooltip)
        self.le_user.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.le_user.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.le_user.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.le_user.setText("")
        self.le_user.setPlaceholderText(QCoreApplication.translate("Parent", u"ex. user@company.com", None))
        self.lb_password.setText("")
#if QT_CONFIG(tooltip)
        self.le_password.setToolTip(QCoreApplication.translate("Parent", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">If you </span><span style=\" font-size:10pt; font-weight:700;\">don't</span><span style=\" font-size:10pt;\"> have a </span><span style=\" font-size:10pt; font-weight:700;\">FaultID account</span><span style=\" font-size:10pt;\">, please </span><span style=\" font-size:10pt; font-weight:700;\">contact your manager</span><span style=\" font-size:10pt;\">.</span></p></"
                        "body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.le_password.setPlaceholderText(QCoreApplication.translate("Parent", u"Your secret password", None))
#if QT_CONFIG(accessibility)
        self.lb_warning_icon.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.lb_warning_icon.setText("")
        self.lb_warning_message.setText(QCoreApplication.translate("Parent", u"Credentials are not correct!", None))
        self.pb_log_in.setText(QCoreApplication.translate("Parent", u" Log in", None))
    # retranslateUi

