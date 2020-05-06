# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'travel_assistant.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import travel_assistant_assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 600)
        icon = QIcon()
        icon.addFile(u":/Icons/assets/planeIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.views = QStackedWidget(self.centralwidget)
        self.views.setObjectName(u"views")
        self.welcome = QWidget()
        self.welcome.setObjectName(u"welcome")
        self.gridLayout_2 = QGridLayout(self.welcome)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame = QFrame(self.welcome)
        self.frame.setObjectName(u"frame")
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"QFrame \n"
"{\n"
"image: url(:/Images/assets/plane_vector.png);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.1875, x2:1, y2:1, stop:0 rgba(49, 139, 180, 255), stop:1 rgba(0, 0, 0, 255));\n"
"}\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(248, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.travel_button = QPushButton(self.frame)
        self.travel_button.setObjectName(u"travel_button")
        self.travel_button.setMinimumSize(QSize(200, 60))
        self.travel_button.setMaximumSize(QSize(200, 100))
        font = QFont()
        font.setFamily(u"News706 BT")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.travel_button.setFont(font)
        self.travel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.travel_button.setStyleSheet(u"QPushButton{\n"
"	selection-background-color: rgb(85, 255, 255);\n"
"	selection-color: rgb(170, 0, 0);\n"
"\n"
"}")
        self.travel_button.setIcon(icon)
        self.travel_button.setAutoDefault(False)
        self.travel_button.setFlat(False)

        self.gridLayout_3.addWidget(self.travel_button, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(278, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.views.addWidget(self.welcome)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_4 = QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_2 = QFrame(self.page_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_11 = QSpacerItem(120, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 0, 0, 1, 2)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"News706 BT")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 0, 2, 1, 1)

        self.graphicsView = QGraphicsView(self.frame_2)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(0, 0))
        self.graphicsView.setMaximumSize(QSize(950, 16777215))
        self.graphicsView.setStyleSheet(u"QGraphicsView\n"
"{\n"
"	background-color: None;\n"
"	border-image: url(:/Images/assets/worldmap.jpg);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.graphicsView, 1, 1, 1, 3)

        self.horizontalSpacer_12 = QSpacerItem(271, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setMaximumSize(QSize(950, 16777215))
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(73, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 0, 2, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 0, 3, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 0, 4, 1, 1)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_5.addWidget(self.pushButton, 0, 5, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 1, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.comboBox, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(73, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.gridLayout_5.addWidget(self.radioButton, 1, 3, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 1, 4, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 0))

        self.gridLayout_5.addWidget(self.comboBox_2, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(73, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.radioButton_3 = QRadioButton(self.groupBox)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.gridLayout_5.addWidget(self.radioButton_3, 2, 3, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(72, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 2, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_5.addWidget(self.pushButton_2, 2, 5, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 2, 1, 1, 3)

        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(275, 16777215))

        self.gridLayout_6.addWidget(self.listWidget, 1, 0, 2, 1)


        self.gridLayout_4.addWidget(self.frame_2, 0, 1, 1, 1)

        self.views.addWidget(self.page_2)

        self.gridLayout.addWidget(self.views, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 860, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.views.setCurrentIndex(1)
        self.travel_button.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Travel Assistant", None))
        self.travel_button.setText(QCoreApplication.translate("MainWindow", u"TRAVEL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"WORLD TOUR", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Reservation", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Specifications", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Departure:", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Money", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Arrival:", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Distance", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
    # retranslateUi

