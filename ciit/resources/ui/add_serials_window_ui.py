# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_serials_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_add_serials_window(object):
    def setupUi(self, add_serials_window):
        if not add_serials_window.objectName():
            add_serials_window.setObjectName(u"add_serials_window")
        add_serials_window.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(add_serials_window.sizePolicy().hasHeightForWidth())
        add_serials_window.setSizePolicy(sizePolicy)
        add_serials_window.setMinimumSize(QSize(960, 540))
        add_serials_window.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Vitesco"])
        font.setPointSize(12)
        add_serials_window.setFont(font)
        add_serials_window.setStyleSheet(u"QPushButton {\n"
"border-radius: 12px;\n"
"padding-left: 16px;\n"
"padding-right: 16px;\n"
"padding-top: 8 px;\n"
"padding-bottom: 8 px;\n"
"}")
        self.gridLayout = QGridLayout(add_serials_window)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.vl_bottom = QVBoxLayout()
        self.vl_bottom.setSpacing(6)
        self.vl_bottom.setObjectName(u"vl_bottom")
        self.vl_bottom.setContentsMargins(-1, 0, -1, -1)
        self.lb_error = QLabel(add_serials_window)
        self.lb_error.setObjectName(u"lb_error")
        self.lb_error.setEnabled(False)
        self.lb_error.setFont(font)
        self.lb_error.setStyleSheet(u"QLabel\n"
"{\n"
"color: rgba(227, 45, 0, 255);\n"
"}\n"
"QLabel:disabled\n"
"{\n"
"color: rgba(227, 45, 0, 0);\n"
"}")
        self.lb_error.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lb_error.setWordWrap(True)

        self.vl_bottom.addWidget(self.lb_error, 0, Qt.AlignmentFlag.AlignBottom)

        self.le_serials = QLineEdit(add_serials_window)
        self.le_serials.setObjectName(u"le_serials")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.le_serials.sizePolicy().hasHeightForWidth())
        self.le_serials.setSizePolicy(sizePolicy1)
        self.le_serials.setMinimumSize(QSize(128, 34))
        self.le_serials.setMaximumSize(QSize(512, 34))
        self.le_serials.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(12)
        self.le_serials.setFont(font1)
        self.le_serials.setStyleSheet(u"color: black;\n"
"background-color: #9EAEAE;\n"
"border-radius: 12px;\n"
"padding: 8px 32px;\n"
"")
        self.le_serials.setInputMask(u"")
        self.le_serials.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vl_bottom.addWidget(self.le_serials, 0, Qt.AlignmentFlag.AlignVCenter)

        self.hl_bottom = QHBoxLayout()
        self.hl_bottom.setObjectName(u"hl_bottom")
        self.pb_import = QPushButton(add_serials_window)
        self.pb_import.setObjectName(u"pb_import")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_import.sizePolicy().hasHeightForWidth())
        self.pb_import.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setKerning(True)
        self.pb_import.setFont(font2)
        self.pb_import.setStyleSheet(u"QPushButton {\n"
"	\n"
"	background-color: rgb(64, 130, 100);\n"
"    }\n"
"QPushButton:disabled {\n"
"	background-color: rgba(64, 130, 100, 150);\n"
"    }\n"
"    QPushButton:hover {\n"
"	\n"
"	\n"
"	background-color: rgb(53, 108, 83);\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"	\n"
"	\n"
"	background-color: rgb(40, 80, 61);\n"
"    }")

        self.hl_bottom.addWidget(self.pb_import)

        self.pb_continue = QPushButton(add_serials_window)
        self.pb_continue.setObjectName(u"pb_continue")
        self.pb_continue.setEnabled(False)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pb_continue.sizePolicy().hasHeightForWidth())
        self.pb_continue.setSizePolicy(sizePolicy3)
        self.pb_continue.setMinimumSize(QSize(64, 0))
        self.pb_continue.setMaximumSize(QSize(128, 16777215))
        self.pb_continue.setFont(font)
        self.pb_continue.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(64, 130, 100);\n"
"    }\n"
"\n"
"    QPushButton:disabled {\n"
"	background-color: rgba(0,0,0,0);\n"
"	color:  rgba(0,0,0,0);\n"
"    }\n"
"    QPushButton:hover {\n"
"	\n"
"	\n"
"	background-color: rgb(53, 108, 83);\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"	\n"
"	\n"
"	background-color: rgb(40, 80, 61);\n"
"    }")

        self.hl_bottom.addWidget(self.pb_continue)


        self.vl_bottom.addLayout(self.hl_bottom)


        self.gridLayout.addLayout(self.vl_bottom, 11, 1, 1, 1)

        self.lb_title = QLabel(add_serials_window)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Vitesco"])
        font3.setPointSize(32)
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.lb_title.setFont(font3)
        self.lb_title.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(226, 220, 220);\n"
"}")
        self.lb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_title, 1, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.vl_center = QVBoxLayout()
        self.vl_center.setSpacing(16)
        self.vl_center.setObjectName(u"vl_center")
        self.lw_serials = QListWidget(add_serials_window)
        self.lw_serials.setObjectName(u"lw_serials")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lw_serials.sizePolicy().hasHeightForWidth())
        self.lw_serials.setSizePolicy(sizePolicy4)
        self.lw_serials.setMinimumSize(QSize(256, 256))
        self.lw_serials.setMaximumSize(QSize(512, 256))
        self.lw_serials.setSizeIncrement(QSize(2, 2))
        font4 = QFont()
        font4.setFamilies([u"Vitesco"])
        font4.setPointSize(14)
        font4.setStrikeOut(False)
        self.lw_serials.setFont(font4)
        self.lw_serials.setStyleSheet(u"QListWidget {\n"
"    background-color: #384C53;\n"
"    border-radius: 30px;\n"
"    outline: 0px;\n"
"    color: rgb(230, 230, 230);\n"
"    padding-right: 20px; /* Add padding to accommodate the scrollbar */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    margin: 8px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QListWidget::item::hover {\n"
"    color: rgb(197, 197, 197);\n"
"    font: bold;\n"
"}\n"
"\n"
"QListWidget::item::selected {\n"
"    color: rgb(212, 39, 0);\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"	background-color: #344955;\n"
"	width: 10px;\n"
"    margin-top: 1px;\n"
"	margin-bottom: 1px;\n"
"	border-radius: 10px;\n"
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
" "
                        "   background-color: rgba(0, 0, 0, 0);\n"
"    height: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical,\n"
"QScrollBar::sub-page:vertical {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"")
        self.lw_serials.setFrameShape(QFrame.Shape.StyledPanel)
        self.lw_serials.setFrameShadow(QFrame.Shadow.Raised)
        self.lw_serials.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.lw_serials.setAlternatingRowColors(False)
        self.lw_serials.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.lw_serials.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)

        self.vl_center.addWidget(self.lw_serials)

        self.hl_center = QHBoxLayout()
        self.hl_center.setSpacing(8)
        self.hl_center.setObjectName(u"hl_center")
        self.pb_delete = QPushButton(add_serials_window)
        self.pb_delete.setObjectName(u"pb_delete")
        self.pb_delete.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.pb_delete.sizePolicy().hasHeightForWidth())
        self.pb_delete.setSizePolicy(sizePolicy2)
        self.pb_delete.setMaximumSize(QSize(256, 16777215))
        self.pb_delete.setFont(font1)
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

        self.hl_center.addWidget(self.pb_delete, 0, Qt.AlignmentFlag.AlignTop)

        self.pb_clear = QPushButton(add_serials_window)
        self.pb_clear.setObjectName(u"pb_clear")
        self.pb_clear.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pb_clear.sizePolicy().hasHeightForWidth())
        self.pb_clear.setSizePolicy(sizePolicy3)
        self.pb_clear.setMaximumSize(QSize(192, 16777215))
        self.pb_clear.setFont(font1)
        self.pb_clear.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(158, 174, 174);\n"
"	color: rgb(75,75,70)\n"
"    }\n"
"QPushButton:disabled {\n"
"	background-color: rgba(158, 174, 174, 100);\n"
"	color: rgb(43, 43, 43);\n"
"    }\n"
"\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgb(138, 152, 152);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(115, 126, 126);\n"
"    }")

        self.hl_center.addWidget(self.pb_clear, 0, Qt.AlignmentFlag.AlignTop)


        self.vl_center.addLayout(self.hl_center)


        self.gridLayout.addLayout(self.vl_center, 2, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.pb_info = QPushButton(add_serials_window)
        self.pb_info.setObjectName(u"pb_info")
        self.pb_info.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	padding-left: 16px;\n"
"	padding-right: 16px;\n"
"	padding-top: 8 px;\n"
"	padding-bottom: 8 px;\n"
"	color: rgb(226, 220, 220);\n"
"	background-color: #384C53\n"
"    }\n"
"")

        self.horizontalLayout.addWidget(self.pb_info, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)

        QWidget.setTabOrder(self.lw_serials, self.le_serials)
        QWidget.setTabOrder(self.le_serials, self.pb_delete)
        QWidget.setTabOrder(self.pb_delete, self.pb_clear)

        self.retranslateUi(add_serials_window)

        QMetaObject.connectSlotsByName(add_serials_window)
    # setupUi

    def retranslateUi(self, add_serials_window):
        add_serials_window.setWindowTitle(QCoreApplication.translate("add_serials_window", u"CIIT", None))
        self.lb_error.setText(QCoreApplication.translate("add_serials_window", u"The serial entered is not valid! Please try another!", None))
        self.le_serials.setText("")
        self.le_serials.setPlaceholderText(QCoreApplication.translate("add_serials_window", u"Write serials here", None))
        self.pb_import.setText(QCoreApplication.translate("add_serials_window", u"Import from Excel", None))
        self.pb_continue.setText(QCoreApplication.translate("add_serials_window", u"Continue", None))
        self.lb_title.setText(QCoreApplication.translate("add_serials_window", u"Add serials", None))
        self.pb_delete.setText(QCoreApplication.translate("add_serials_window", u"Delete selected", None))
        self.pb_clear.setText(QCoreApplication.translate("add_serials_window", u"Clear list", None))
        self.pb_info.setText(QCoreApplication.translate("add_serials_window", u"Info", None))
    # retranslateUi

