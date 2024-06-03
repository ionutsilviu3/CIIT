# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_window.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_settings_window(object):
    def setupUi(self, settings_window):
        if not settings_window.objectName():
            settings_window.setObjectName(u"settings_window")
        settings_window.resize(960, 540)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings_window.sizePolicy().hasHeightForWidth())
        settings_window.setSizePolicy(sizePolicy)
        settings_window.setMinimumSize(QSize(960, 540))
        settings_window.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Vitesco"])
        font.setPointSize(12)
        settings_window.setFont(font)
        settings_window.setStyleSheet(u"QPushButton {\n"
"border-radius: 12px;\n"
"padding-left: 16px;\n"
"padding-right: 16px;\n"
"padding-top: 8 px;\n"
"padding-bottom: 8 px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"	font: 12pt Roboto;\n"
"	color: rgb(158, 174, 174);\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"	background-color: rgb(158, 174, 174);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QRadioButton#rb_low_input::indicator:checked,\n"
" QRadioButton#rb_low_other::indicator:checked{\n"
"   \n"
"	background-color: rgb(64, 130, 100);\n"
"}\n"
"\n"
"QRadioButton#rb_normal_input::indicator:checked,\n"
" QRadioButton#rb_normal_other::indicator:checked {\n"
"   \n"
"	background-color: rgb(249, 248, 113);\n"
"}\n"
"\n"
"QRadioButton#rb_high_input::indicator:checked,\n"
" QRadioButton#rb_high_other::indicator:checked {\n"
"   background-color: rgb(138, 29, 0);\n"
"}\n"
"")
        self.gridLayout = QGridLayout(settings_window)
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(8, 8, 8, 8)
        self.vl_contents = QVBoxLayout()
        self.vl_contents.setSpacing(16)
        self.vl_contents.setObjectName(u"vl_contents")
        self.vl_contents.setContentsMargins(24, 24, 24, 48)
        self.lb_overview_title = QLabel(settings_window)
        self.lb_overview_title.setObjectName(u"lb_overview_title")
        font1 = QFont()
        font1.setFamilies([u"Roboto"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.lb_overview_title.setFont(font1)
        self.lb_overview_title.setStyleSheet(u"color: rgb(226, 220, 220);")

        self.vl_contents.addWidget(self.lb_overview_title, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.fl_overview = QFormLayout()
        self.fl_overview.setObjectName(u"fl_overview")
        self.fl_overview.setHorizontalSpacing(24)
        self.fl_overview.setVerticalSpacing(24)
        self.lb_limit_sensitivity = QLabel(settings_window)
        self.lb_limit_sensitivity.setObjectName(u"lb_limit_sensitivity")
        font2 = QFont()
        font2.setFamilies([u"Roboto"])
        font2.setPointSize(12)
        self.lb_limit_sensitivity.setFont(font2)
        self.lb_limit_sensitivity.setStyleSheet(u"color:rgb(226, 220, 220);")

        self.fl_overview.setWidget(0, QFormLayout.LabelRole, self.lb_limit_sensitivity)

        self.sb_limit_sensitivity = QSpinBox(settings_window)
        self.sb_limit_sensitivity.setObjectName(u"sb_limit_sensitivity")
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.sb_limit_sensitivity.setFont(font3)
        self.sb_limit_sensitivity.setStyleSheet(u"color: rgb(226, 220, 220);")
        self.sb_limit_sensitivity.setWrapping(False)
        self.sb_limit_sensitivity.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.sb_limit_sensitivity.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.sb_limit_sensitivity.setAccelerated(True)
        self.sb_limit_sensitivity.setMaximum(100)
        self.sb_limit_sensitivity.setValue(5)

        self.fl_overview.setWidget(0, QFormLayout.FieldRole, self.sb_limit_sensitivity)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.fl_overview.setItem(1, QFormLayout.LabelRole, self.verticalSpacer)


        self.vl_contents.addLayout(self.fl_overview)

        self.lb_advanced_overview_title = QLabel(settings_window)
        self.lb_advanced_overview_title.setObjectName(u"lb_advanced_overview_title")
        self.lb_advanced_overview_title.setFont(font1)
        self.lb_advanced_overview_title.setStyleSheet(u"color: rgb(226, 220, 220);")

        self.vl_contents.addWidget(self.lb_advanced_overview_title)

        self.fl_advanced = QFormLayout()
        self.fl_advanced.setObjectName(u"fl_advanced")
        self.fl_advanced.setHorizontalSpacing(24)
        self.fl_advanced.setVerticalSpacing(24)
        self.lb_timeframe = QLabel(settings_window)
        self.lb_timeframe.setObjectName(u"lb_timeframe")
        self.lb_timeframe.setFont(font2)
        self.lb_timeframe.setStyleSheet(u"color: rgb(226, 220, 220);")

        self.fl_advanced.setWidget(0, QFormLayout.LabelRole, self.lb_timeframe)

        self.sb_timeframe = QSpinBox(settings_window)
        self.sb_timeframe.setObjectName(u"sb_timeframe")
        self.sb_timeframe.setFont(font2)
        self.sb_timeframe.setStyleSheet(u"color: rgb(226, 220, 220);")
        self.sb_timeframe.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.sb_timeframe.setMinimum(1)
        self.sb_timeframe.setMaximum(8)

        self.fl_advanced.setWidget(0, QFormLayout.FieldRole, self.sb_timeframe)

        self.lb_input_sensitivity = QLabel(settings_window)
        self.lb_input_sensitivity.setObjectName(u"lb_input_sensitivity")
        self.lb_input_sensitivity.setFont(font2)
        self.lb_input_sensitivity.setStyleSheet(u"color: rgb(226, 220, 220);")

        self.fl_advanced.setWidget(1, QFormLayout.LabelRole, self.lb_input_sensitivity)

        self.lb_other_sensitivity = QLabel(settings_window)
        self.lb_other_sensitivity.setObjectName(u"lb_other_sensitivity")
        self.lb_other_sensitivity.setFont(font2)
        self.lb_other_sensitivity.setStyleSheet(u"color: rgb(226, 220, 220);")

        self.fl_advanced.setWidget(3, QFormLayout.LabelRole, self.lb_other_sensitivity)

        self.gb_input_sensitivity = QGroupBox(settings_window)
        self.gb_input_sensitivity.setObjectName(u"gb_input_sensitivity")
        self.gb_input_sensitivity.setStyleSheet(u"QGroupBox {\n"
"    border-radius: 16px;	\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"	border-color:  rgb(64, 130, 100);\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.gb_input_sensitivity)
        self.horizontalLayout_6.setSpacing(16)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(8, 8, 8, 8)
        self.rb_low_input = QRadioButton(self.gb_input_sensitivity)
        self.rb_low_input.setObjectName(u"rb_low_input")
        font4 = QFont()
        font4.setFamilies([u"Roboto"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.rb_low_input.setFont(font4)

        self.horizontalLayout_6.addWidget(self.rb_low_input)

        self.rb_normal_input = QRadioButton(self.gb_input_sensitivity)
        self.rb_normal_input.setObjectName(u"rb_normal_input")
        self.rb_normal_input.setChecked(True)

        self.horizontalLayout_6.addWidget(self.rb_normal_input)

        self.rb_high_input = QRadioButton(self.gb_input_sensitivity)
        self.rb_high_input.setObjectName(u"rb_high_input")

        self.horizontalLayout_6.addWidget(self.rb_high_input)


        self.fl_advanced.setWidget(1, QFormLayout.FieldRole, self.gb_input_sensitivity)

        self.gb_other_sensitivity = QGroupBox(settings_window)
        self.gb_other_sensitivity.setObjectName(u"gb_other_sensitivity")
        self.gb_other_sensitivity.setStyleSheet(u"QGroupBox {\n"
"    border-radius: 16px;	\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"	border-color:  rgb(64, 130, 100);\n"
"}")
        self.horizontalLayout_7 = QHBoxLayout(self.gb_other_sensitivity)
        self.horizontalLayout_7.setSpacing(16)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(8, 8, 8, 8)
        self.rb_low_other = QRadioButton(self.gb_other_sensitivity)
        self.rb_low_other.setObjectName(u"rb_low_other")

        self.horizontalLayout_7.addWidget(self.rb_low_other)

        self.rb_normal_other = QRadioButton(self.gb_other_sensitivity)
        self.rb_normal_other.setObjectName(u"rb_normal_other")
        self.rb_normal_other.setChecked(True)

        self.horizontalLayout_7.addWidget(self.rb_normal_other)

        self.rb_high_other = QRadioButton(self.gb_other_sensitivity)
        self.rb_high_other.setObjectName(u"rb_high_other")

        self.horizontalLayout_7.addWidget(self.rb_high_other)


        self.fl_advanced.setWidget(3, QFormLayout.FieldRole, self.gb_other_sensitivity)


        self.vl_contents.addLayout(self.fl_advanced)


        self.gridLayout.addLayout(self.vl_contents, 3, 1, 1, 1)

        self.lb_title = QLabel(settings_window)
        self.lb_title.setObjectName(u"lb_title")
        self.lb_title.setMaximumSize(QSize(16777215, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Roboto"])
        font5.setPointSize(32)
        font5.setBold(True)
        font5.setStrikeOut(False)
        self.lb_title.setFont(font5)
        self.lb_title.setStyleSheet(u"QLabel\n"
"{\n"
"	color: rgb(226, 220, 220);\n"
"}")
        self.lb_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lb_title, 1, 0, 1, 3, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.vs_bottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.vs_bottom, 13, 1, 1, 1)

        self.pb_save = QPushButton(settings_window)
        self.pb_save.setObjectName(u"pb_save")
        self.pb_save.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pb_save.sizePolicy().hasHeightForWidth())
        self.pb_save.setSizePolicy(sizePolicy1)
        self.pb_save.setMinimumSize(QSize(64, 0))
        self.pb_save.setMaximumSize(QSize(128, 16777215))
        self.pb_save.setFont(font2)
        self.pb_save.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(64, 130, 100);\n"
"	color: rgb(226, 220, 220);\n"
"    }\n"
"    QPushButton:hover {\n"
"	background-color: rgb(51, 104, 79);\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"	\n"
"	background-color: rgb(36, 72, 55);\n"
"    }\n"
"QPushButton:disabled{\n"
"	\n"
"	background-color: rgba(64, 130, 100, 150);\n"
"    }")

        self.gridLayout.addWidget(self.pb_save, 12, 1, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pb_back = QPushButton(settings_window)
        self.pb_back.setObjectName(u"pb_back")
        self.pb_back.setFont(font2)
        self.pb_back.setStyleSheet(u"QPushButton {\n"
"border-radius: 12px;\n"
"background-color: rgb(53, 76, 88);\n"
"color: rgb(190, 190, 190);\n"
"padding-left: 16px;\n"
"padding-right: 16px;\n"
"padding-top: 8 px;\n"
"padding-bottom: 8 px;\n"
"}")

        self.gridLayout.addWidget(self.pb_back, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        QWidget.setTabOrder(self.pb_back, self.pb_save)
        QWidget.setTabOrder(self.pb_save, self.rb_low_input)
        QWidget.setTabOrder(self.rb_low_input, self.sb_timeframe)
        QWidget.setTabOrder(self.sb_timeframe, self.sb_limit_sensitivity)
        QWidget.setTabOrder(self.sb_limit_sensitivity, self.rb_normal_input)
        QWidget.setTabOrder(self.rb_normal_input, self.rb_high_input)
        QWidget.setTabOrder(self.rb_high_input, self.rb_low_other)
        QWidget.setTabOrder(self.rb_low_other, self.rb_normal_other)
        QWidget.setTabOrder(self.rb_normal_other, self.rb_high_other)

        self.retranslateUi(settings_window)

        QMetaObject.connectSlotsByName(settings_window)
    # setupUi

    def retranslateUi(self, settings_window):
        settings_window.setWindowTitle(QCoreApplication.translate("settings_window", u"CIIT", None))
        self.lb_overview_title.setText(QCoreApplication.translate("settings_window", u"Overview Page Settings", None))
        self.lb_limit_sensitivity.setText(QCoreApplication.translate("settings_window", u"Limits sensitivity level", None))
        self.sb_limit_sensitivity.setSuffix(QCoreApplication.translate("settings_window", u" %", None))
        self.lb_advanced_overview_title.setText(QCoreApplication.translate("settings_window", u"Advanced Overview Page Settings", None))
        self.lb_timeframe.setText(QCoreApplication.translate("settings_window", u"Timeframe of produced parts: ", None))
        self.sb_timeframe.setSuffix(QCoreApplication.translate("settings_window", u" hours", None))
        self.lb_input_sensitivity.setText(QCoreApplication.translate("settings_window", u"Input parts outlier detection sensitivity:", None))
        self.lb_other_sensitivity.setText(QCoreApplication.translate("settings_window", u"Other parts outlier detection sensitivity:", None))
        self.gb_input_sensitivity.setTitle("")
        self.rb_low_input.setText(QCoreApplication.translate("settings_window", u"Low", None))
        self.rb_normal_input.setText(QCoreApplication.translate("settings_window", u"Normal", None))
        self.rb_high_input.setText(QCoreApplication.translate("settings_window", u"High", None))
        self.gb_other_sensitivity.setTitle("")
        self.rb_low_other.setText(QCoreApplication.translate("settings_window", u"Low", None))
        self.rb_normal_other.setText(QCoreApplication.translate("settings_window", u"Normal", None))
        self.rb_high_other.setText(QCoreApplication.translate("settings_window", u"High", None))
        self.lb_title.setText(QCoreApplication.translate("settings_window", u"Settings", None))
        self.pb_save.setText(QCoreApplication.translate("settings_window", u"Save", None))
        self.pb_back.setText(QCoreApplication.translate("settings_window", u"Go back", None))
    # retranslateUi

