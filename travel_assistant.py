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
        MainWindow.resize(800, 600)
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
        self.frame.setCursor(QCursor(Qt.UpArrowCursor))
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
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"News706 BT")
        font1.setPointSize(72)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.views.addWidget(self.page_2)

        self.gridLayout.addWidget(self.views, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.travel_button.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Travel Assistant", None))
        self.travel_button.setText(QCoreApplication.translate("MainWindow", u"TRAVEL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"UwU", None))
    # retranslateUi

