# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_admin_overview(object):
    def setupUi(self, admin_overview):
        if not admin_overview.objectName():
            admin_overview.setObjectName(u"admin_overview")
        admin_overview.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(admin_overview.sizePolicy().hasHeightForWidth())
        admin_overview.setSizePolicy(sizePolicy)
        admin_overview.setMinimumSize(QSize(960, 540))
        admin_overview.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Vitesco"])
        font.setPointSize(12)
        admin_overview.setFont(font)
        admin_overview.setStyleSheet(u"QPushButton {\n"
"border-radius: 12px;\n"
"padding-left: 16px;\n"
"padding-right: 16px;\n"
"padding-top: 8 px;\n"
"padding-bottom: 8 px;\n"
"}")
        self.gridLayout = QGridLayout(admin_overview)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.lb_title = QLabel(admin_overview)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(26)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.lb_title.setFont(font1)
        self.lb_title.setStyleSheet(u"QLabel\n"
"{\n"
"	\n"
"	color: rgb(190, 190, 190);\n"
"}")
        self.lb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_title, 0, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)

        self.vl_center = QVBoxLayout()
        self.vl_center.setSpacing(16)
        self.vl_center.setObjectName(u"vl_center")
        self.tw_users = QTableWidget(admin_overview)
        if (self.tw_users.rowCount() < 1):
            self.tw_users.setRowCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tw_users.setVerticalHeaderItem(0, __qtablewidgetitem)
        self.tw_users.setObjectName(u"tw_users")
        self.tw_users.setMaximumSize(QSize(512, 16777215))
        self.tw_users.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(34, 48, 56);\n"
"    border: none;\n"
"    font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    padding: 12px;\n"
"    color: rgb(226, 220, 220);\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"	padding: 12px;\n"
"    background-color: rgb(64, 130, 100);\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #384C53;\n"
"    color: rgb(226, 220, 220);\n"
"    padding: 5px;\n"
"    border: none;\n"
"    font: 12pt \"Roboto\";\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"	border-left: 1px solid rgb(34, 48, 56);\n"
"}\n"
"")
        self.tw_users.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tw_users.setAlternatingRowColors(False)
        self.tw_users.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tw_users.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tw_users.setSortingEnabled(True)
        self.tw_users.setCornerButtonEnabled(False)

        self.vl_center.addWidget(self.tw_users, 0, Qt.AlignmentFlag.AlignHCenter)

        self.pb_modify_role = QPushButton(admin_overview)
        self.pb_modify_role.setObjectName(u"pb_modify_role")
        self.pb_modify_role.setEnabled(False)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        self.pb_modify_role.setFont(font2)
        self.pb_modify_role.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(158, 174, 174);\n"
"color: rgb(138, 29, 0);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: rgba(158, 174, 174, 0);\n"
"color: rgba(138, 29, 0, 0);\n"
"}")

        self.vl_center.addWidget(self.pb_modify_role, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pb_delete = QPushButton(admin_overview)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_delete.sizePolicy().hasHeightForWidth())
        self.pb_delete.setSizePolicy(sizePolicy1)
        self.pb_delete.setMaximumSize(QSize(256, 16777215))
        self.pb_delete.setFont(font2)
        self.pb_delete.setStyleSheet(u"QPushButton {\n"
"	color: rgb(226, 220, 220);\n"
"	background-color: rgb(138, 29, 0)\n"
"    }\n"
"QPushButton:disabled {\n"
"	background-color: rgba(109, 22, 0, 200);\n"
"    }\n"
"    QPushButton:hover {\n"
"	background-color: rgb(120, 24, 0);\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"	background-color: rgb(94, 19, 0);\n"
"    }")

        self.vl_center.addWidget(self.pb_delete, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lb_message = QLabel(admin_overview)
        self.lb_message.setObjectName(u"lb_message")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(10)
        self.lb_message.setFont(font3)
        self.lb_message.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(226, 220, 220);\n"
"}")

        self.vl_center.addWidget(self.lb_message, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.le_users = QLineEdit(admin_overview)
        self.le_users.setObjectName(u"le_users")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_users.sizePolicy().hasHeightForWidth())
        self.le_users.setSizePolicy(sizePolicy2)
        self.le_users.setMinimumSize(QSize(128, 34))
        self.le_users.setMaximumSize(QSize(512, 34))
        self.le_users.setSizeIncrement(QSize(0, 0))
        self.le_users.setFont(font2)
        self.le_users.setStyleSheet(u"QLineEdit\n"
"{\n"
"color: rgb(26, 39, 39);\n"
"background-color: rgb(158, 174, 174);\n"
"border-radius: 12px;\n"
"padding: 8px 32px\n"
"}\n"
"")
        self.le_users.setInputMask(u"")
        self.le_users.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vl_center.addWidget(self.le_users)

        self.hl_center = QHBoxLayout()
        self.hl_center.setSpacing(8)
        self.hl_center.setObjectName(u"hl_center")
        self.pb_add = QPushButton(admin_overview)
        self.pb_add.setObjectName(u"pb_add")
        self.pb_add.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.pb_add.sizePolicy().hasHeightForWidth())
        self.pb_add.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setKerning(True)
        self.pb_add.setFont(font4)
        self.pb_add.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(64, 130, 100);\n"
"	color: rgb(226, 220, 220)\n"
"    }\n"
"QPushButton:disabled {\n"
"	background-color: rgba(46, 94, 72, 200);\n"
"	color: rgba(226, 220, 220, 100);\n"
"    }\n"
"    QPushButton:hover {\n"
"	\n"
"	background-color: rgb(30, 107, 36);\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(27, 97, 33);\n"
"    }")

        self.hl_center.addWidget(self.pb_add, 0, Qt.AlignmentFlag.AlignHCenter)


        self.vl_center.addLayout(self.hl_center)


        self.gridLayout.addLayout(self.vl_center, 1, 1, 1, 1)

        self.vl_chart = QVBoxLayout()
        self.vl_chart.setObjectName(u"vl_chart")
        self.pb_main_app = QPushButton(admin_overview)
        self.pb_main_app.setObjectName(u"pb_main_app")
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.pb_main_app.setFont(font5)
        self.pb_main_app.setStyleSheet(u"QPushButton {\n"
"	border-radius: 16px;\n"
"	padding-left: 8px;\n"
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
        icon = QIcon()
        icon.addFile(u":/Icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_main_app.setIcon(icon)
        self.pb_main_app.setIconSize(QSize(24, 24))

        self.vl_chart.addWidget(self.pb_main_app, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.gridLayout.addLayout(self.vl_chart, 1, 2, 1, 1)


        self.retranslateUi(admin_overview)

        QMetaObject.connectSlotsByName(admin_overview)
    # setupUi

    def retranslateUi(self, admin_overview):
        admin_overview.setWindowTitle(QCoreApplication.translate("admin_overview", u"CIIT", None))
        self.lb_title.setText(QCoreApplication.translate("admin_overview", u"Admin", None))
        self.pb_modify_role.setText(QCoreApplication.translate("admin_overview", u"Remove manager role", None))
        self.pb_delete.setText(QCoreApplication.translate("admin_overview", u"Delete User", None))
        self.lb_message.setText("")
        self.le_users.setText("")
        self.le_users.setPlaceholderText(QCoreApplication.translate("admin_overview", u"Add user by email", None))
        self.pb_add.setText(QCoreApplication.translate("admin_overview", u"Add user", None))
        self.pb_main_app.setText(QCoreApplication.translate("admin_overview", u"Go to main app", None))
    # retranslateUi

