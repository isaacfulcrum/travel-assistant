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
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QSize(1000, 700))
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
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_12 = QGridLayout(self.page)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"border-image:url(:/Images/assets/city_map.jpg);\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.backbutton_1 = QPushButton(self.frame_5)
        self.backbutton_1.setObjectName(u"backbutton_1")
        self.backbutton_1.setMinimumSize(QSize(0, 40))
        self.backbutton_1.setMaximumSize(QSize(100, 16777215))
        font1 = QFont()
        font1.setFamily(u"News706 BT")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setWeight(75)
        self.backbutton_1.setFont(font1)
        self.backbutton_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.backbutton_1.setStyleSheet(u"border-image: None;\n"
"background-color: rgb(30, 177, 167);")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/assets/backIcon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.backbutton_1.setIcon(icon1)

        self.gridLayout_14.addWidget(self.backbutton_1, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_4, 1, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_17, 2, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(660, 300))
        self.frame_6.setMaximumSize(QSize(700, 400))
        self.frame_6.setStyleSheet(u"border-image:None;\n"
"background-color: rgb(0, 0, 0);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_6)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        font2 = QFont()
        font2.setFamily(u"News706 BT")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"border-image: None;\n"
"background-color: rgb(255, 255, 255);")
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setWordWrap(True)

        self.gridLayout_13.addWidget(self.label_16, 0, 0, 1, 1)


        self.gridLayout_14.addWidget(self.frame_6, 2, 1, 1, 3)

        self.horizontalSpacer_18 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_18, 2, 4, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 87, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_5, 3, 2, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_20, 4, 0, 1, 1)

        self.personalized_button = QPushButton(self.frame_5)
        self.personalized_button.setObjectName(u"personalized_button")
        self.personalized_button.setMinimumSize(QSize(200, 100))
        self.personalized_button.setFont(font1)
        self.personalized_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.personalized_button.setStyleSheet(u"border-image: None;\n"
"background-color: rgb(127, 7, 179);")

        self.gridLayout_14.addWidget(self.personalized_button, 4, 1, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(245, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_19, 4, 2, 1, 1)

        self.adventure_button = QPushButton(self.frame_5)
        self.adventure_button.setObjectName(u"adventure_button")
        self.adventure_button.setMinimumSize(QSize(200, 100))
        self.adventure_button.setFont(font1)
        self.adventure_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.adventure_button.setStyleSheet(u"background-color: rgb(113, 255, 62);\n"
"border-image: None;")

        self.gridLayout_14.addWidget(self.adventure_button, 4, 3, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(134, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_21, 4, 4, 1, 1)


        self.gridLayout_12.addWidget(self.frame_5, 0, 1, 1, 1)

        self.views.addWidget(self.page)
        self.users = QWidget()
        self.users.setObjectName(u"users")
        self.gridLayout_7 = QGridLayout(self.users)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.frame_3 = QFrame(self.users)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"border-image: url(:/Images/assets/travelStamps.jpg);\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.backbutton_2 = QPushButton(self.frame_3)
        self.backbutton_2.setObjectName(u"backbutton_2")
        self.backbutton_2.setMinimumSize(QSize(0, 40))
        self.backbutton_2.setMaximumSize(QSize(100, 16777215))
        self.backbutton_2.setFont(font1)
        self.backbutton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.backbutton_2.setStyleSheet(u"border-image: None;\n"
"background-color: rgb(30, 177, 167);")
        self.backbutton_2.setIcon(icon1)

        self.gridLayout_11.addWidget(self.backbutton_2, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 83, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(154, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_13, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(620, 370))
        self.frame_4.setStyleSheet(u"background-color:rgb(0, 0, 0);\n"
"border-image:None;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(600, 350))
        self.groupBox_3.setMaximumSize(QSize(800, 350))
        self.groupBox_3.setFont(font1)
        self.groupBox_3.setStyleSheet(u"border-image:None;\n"
"background-color:rgb(66, 148, 170);\n"
"color: rgb(255, 255, 255)\n"
"\n"
"\n"
"\n"
"")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.groupBox_3.setFlat(False)
        self.gridLayout_9 = QGridLayout(self.groupBox_3)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(-1, 9, -1, -1)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(25, 25))
        self.label_6.setStyleSheet(u"image: url(:/Icons/assets/userIcon.png);")

        self.gridLayout_9.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.gridLayout_9.addWidget(self.label_7, 0, 1, 1, 1)

        self.nameText = QLineEdit(self.groupBox_3)
        self.nameText.setObjectName(u"nameText")
        self.nameText.setMinimumSize(QSize(250, 0))
        self.nameText.setMaximumSize(QSize(300, 16777215))
        self.nameText.setStyleSheet(u"background-color: None;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout_9.addWidget(self.nameText, 0, 2, 1, 4)

        self.horizontalSpacer_9 = QSpacerItem(226, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_9, 0, 6, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(25, 25))
        self.label_10.setStyleSheet(u"image: url(:/Icons/assets/moneyIcon.png);")

        self.gridLayout_9.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.gridLayout_9.addWidget(self.label_8, 1, 1, 1, 1)

        self.budgetText = QLineEdit(self.groupBox_3)
        self.budgetText.setObjectName(u"budgetText")
        self.budgetText.setMaximumSize(QSize(100, 16777215))
        self.budgetText.setStyleSheet(u"background-color: None;\n"
"color: rgb(0, 0, 0)")

        self.gridLayout_9.addWidget(self.budgetText, 1, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(381, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_10, 1, 3, 1, 4)

        self.ready_button = QPushButton(self.groupBox_3)
        self.ready_button.setObjectName(u"ready_button")
        self.ready_button.setMaximumSize(QSize(100, 50))
        self.ready_button.setFont(font1)
        self.ready_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.ready_button.setStyleSheet(u"border-image: None\n"
";")
        self.ready_button.setIcon(icon)

        self.gridLayout_9.addWidget(self.ready_button, 3, 4, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(260, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_16, 3, 5, 1, 2)

        self.groupBox_2 = QGroupBox(self.groupBox_3)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setFlat(False)
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.star3_3 = QLabel(self.groupBox_2)
        self.star3_3.setObjectName(u"star3_3")
        self.star3_3.setMaximumSize(QSize(30, 16777215))
        self.star3_3.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star3_3, 2, 5, 1, 1)

        self.food_sb = QSpinBox(self.groupBox_2)
        self.food_sb.setObjectName(u"food_sb")
        self.food_sb.setMaximumSize(QSize(60, 16777215))
        self.food_sb.setStyleSheet(u"background-color:None;\n"
"color: rgb(0, 0, 0)")
        self.food_sb.setMinimum(1)
        self.food_sb.setMaximum(5)

        self.gridLayout_8.addWidget(self.food_sb, 1, 2, 1, 1)

        self.star2_2 = QLabel(self.groupBox_2)
        self.star2_2.setObjectName(u"star2_2")
        self.star2_2.setMaximumSize(QSize(30, 16777215))
        self.star2_2.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star2_2, 1, 4, 1, 1)

        self.star2_4 = QLabel(self.groupBox_2)
        self.star2_4.setObjectName(u"star2_4")
        self.star2_4.setMaximumSize(QSize(30, 16777215))
        self.star2_4.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star2_4, 1, 6, 1, 1)

        self.star1_3 = QLabel(self.groupBox_2)
        self.star1_3.setObjectName(u"star1_3")
        self.star1_3.setMaximumSize(QSize(30, 16777215))
        self.star1_3.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star1_3, 0, 5, 1, 1)

        self.star1_2 = QLabel(self.groupBox_2)
        self.star1_2.setObjectName(u"star1_2")
        self.star1_2.setMaximumSize(QSize(30, 16777215))
        self.star1_2.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star1_2, 0, 4, 1, 1)

        self.label_12 = QLabel(self.groupBox_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_8.addWidget(self.label_12, 1, 1, 1, 1)

        self.star3_2 = QLabel(self.groupBox_2)
        self.star3_2.setObjectName(u"star3_2")
        self.star3_2.setMaximumSize(QSize(30, 16777215))
        self.star3_2.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star3_2, 2, 4, 1, 1)

        self.star1_1 = QLabel(self.groupBox_2)
        self.star1_1.setObjectName(u"star1_1")
        self.star1_1.setMaximumSize(QSize(30, 16777215))
        self.star1_1.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star1_1, 0, 3, 1, 1)

        self.star1_5 = QLabel(self.groupBox_2)
        self.star1_5.setObjectName(u"star1_5")
        self.star1_5.setMaximumSize(QSize(30, 16777215))
        self.star1_5.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star1_5, 0, 7, 1, 1)

        self.star1_4 = QLabel(self.groupBox_2)
        self.star1_4.setObjectName(u"star1_4")
        self.star1_4.setMaximumSize(QSize(30, 16777215))
        self.star1_4.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star1_4, 0, 6, 1, 1)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_8.addWidget(self.label_9, 2, 1, 1, 1)

        self.label_13 = QLabel(self.groupBox_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(30, 16777215))
        self.label_13.setStyleSheet(u"image: url(:/Icons/assets/placeIcon.png);")

        self.gridLayout_8.addWidget(self.label_13, 0, 0, 1, 1)

        self.star2_5 = QLabel(self.groupBox_2)
        self.star2_5.setObjectName(u"star2_5")
        self.star2_5.setMaximumSize(QSize(30, 16777215))
        self.star2_5.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star2_5, 1, 7, 1, 1)

        self.star3_1 = QLabel(self.groupBox_2)
        self.star3_1.setObjectName(u"star3_1")
        self.star3_1.setMaximumSize(QSize(30, 16777215))
        self.star3_1.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star3_1, 2, 3, 1, 1)

        self.label_15 = QLabel(self.groupBox_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"image: url(:/Icons/assets/clothesIcon.png);")

        self.gridLayout_8.addWidget(self.label_15, 2, 0, 1, 1)

        self.places_sb = QSpinBox(self.groupBox_2)
        self.places_sb.setObjectName(u"places_sb")
        self.places_sb.setMaximumSize(QSize(60, 16777215))
        self.places_sb.setStyleSheet(u"background-color:None;\n"
"color: rgb(0, 0, 0)")
        self.places_sb.setMinimum(1)
        self.places_sb.setMaximum(5)

        self.gridLayout_8.addWidget(self.places_sb, 0, 2, 1, 1)

        self.star2_1 = QLabel(self.groupBox_2)
        self.star2_1.setObjectName(u"star2_1")
        self.star2_1.setMaximumSize(QSize(30, 16777215))
        self.star2_1.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star2_1, 1, 3, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(120, 16777215))
        self.label_11.setFont(font1)

        self.gridLayout_8.addWidget(self.label_11, 0, 1, 1, 1)

        self.star2_3 = QLabel(self.groupBox_2)
        self.star2_3.setObjectName(u"star2_3")
        self.star2_3.setMaximumSize(QSize(30, 16777215))
        self.star2_3.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star2_3, 1, 5, 1, 1)

        self.label_14 = QLabel(self.groupBox_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"image: url(:/Icons/assets/foodIcon.png);")

        self.gridLayout_8.addWidget(self.label_14, 1, 0, 1, 1)

        self.star3_4 = QLabel(self.groupBox_2)
        self.star3_4.setObjectName(u"star3_4")
        self.star3_4.setMaximumSize(QSize(30, 16777215))
        self.star3_4.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star3_4, 2, 6, 1, 1)

        self.star3_5 = QLabel(self.groupBox_2)
        self.star3_5.setObjectName(u"star3_5")
        self.star3_5.setMaximumSize(QSize(30, 16777215))
        self.star3_5.setStyleSheet(u"image: url(:/Images/assets/star.png);")

        self.gridLayout_8.addWidget(self.star3_5, 2, 7, 1, 1)

        self.clothes_sb = QSpinBox(self.groupBox_2)
        self.clothes_sb.setObjectName(u"clothes_sb")
        self.clothes_sb.setMaximumSize(QSize(60, 16777215))
        self.clothes_sb.setStyleSheet(u"background-color:None;\n"
"color: rgb(0, 0, 0)")
        self.clothes_sb.setMinimum(1)
        self.clothes_sb.setMaximum(5)

        self.gridLayout_8.addWidget(self.clothes_sb, 2, 2, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_2, 2, 0, 1, 7)

        self.horizontalSpacer_15 = QSpacerItem(227, 47, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_15, 3, 0, 1, 4)


        self.gridLayout_10.addWidget(self.groupBox_3, 0, 0, 1, 1)


        self.gridLayout_11.addWidget(self.frame_4, 2, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(154, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_14, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_2, 3, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)

        self.views.addWidget(self.users)
        self.worldTour = QWidget()
        self.worldTour.setObjectName(u"worldTour")
        self.gridLayout_4 = QGridLayout(self.worldTour)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_2 = QFrame(self.worldTour)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setStyleSheet(u"QFrame \n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:0.1875, x2:1, y2:1, stop:0 rgba(49, 139, 180, 255), stop:1 rgba(0, 0, 0, 255));\n"
"}\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.btnResetMap = QPushButton(self.frame_2)
        self.btnResetMap.setObjectName(u"btnResetMap")
        font3 = QFont()
        font3.setFamily(u"News706 BT")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.btnResetMap.setFont(font3)
        self.btnResetMap.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnResetMap.setStyleSheet(u"background-color: rgb(107, 48, 255);")

        self.gridLayout_6.addWidget(self.btnResetMap, 0, 5, 1, 1)

        self.listWidget = QListWidget(self.frame_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(0, 0))
        self.listWidget.setMaximumSize(QSize(275, 16777215))
        self.listWidget.setStyleSheet(u"background-color:  None;")

        self.gridLayout_6.addWidget(self.listWidget, 1, 0, 2, 1)

        self.gvWorldMap = QGraphicsView(self.frame_2)
        self.gvWorldMap.setObjectName(u"gvWorldMap")
        self.gvWorldMap.setMinimumSize(QSize(950, 400))
        self.gvWorldMap.setMaximumSize(QSize(950, 16777215))
        self.gvWorldMap.setStyleSheet(u"QGraphicsView\n"
"{\n"
"	background-color: None;\n"
"	border-image: url(:/Images/assets/worldmap.jpg);\n"
"}\n"
"")

        self.gridLayout_6.addWidget(self.gvWorldMap, 1, 1, 1, 5)

        self.groupBox = QGroupBox(self.frame_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setMaximumSize(QSize(950, 16777215))
        self.groupBox.setStyleSheet(u"background-color:  rgb(255, 255, 255);")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(70, 16777215))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color:  None;")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)

        self.departure = QComboBox(self.groupBox)
        self.departure.setObjectName(u"departure")
        self.departure.setMinimumSize(QSize(0, 25))
        self.departure.setStyleSheet(u"background-color:  None;")

        self.gridLayout_5.addWidget(self.departure, 0, 1, 1, 1)

        self.start_button = QPushButton(self.groupBox)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(200, 70))
        self.start_button.setMaximumSize(QSize(16777215, 16777215))
        self.start_button.setFont(font3)
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button.setStyleSheet(u"background-color:  rgb(57, 191, 42);")

        self.gridLayout_5.addWidget(self.start_button, 0, 2, 2, 1)

        self.cancel_button = QPushButton(self.groupBox)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(200, 70))
        self.cancel_button.setFont(font3)
        self.cancel_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancel_button.setStyleSheet(u"background-color:  rgb(209, 6, 43);")

        self.gridLayout_5.addWidget(self.cancel_button, 0, 3, 2, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color:  None;")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)

        self.arrival = QComboBox(self.groupBox)
        self.arrival.setObjectName(u"arrival")
        self.arrival.setMinimumSize(QSize(0, 25))
        self.arrival.setStyleSheet(u"background-color:  None;")

        self.gridLayout_5.addWidget(self.arrival, 1, 1, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 2, 1, 1, 5)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"News706 BT")
        font4.setPointSize(24)
        font4.setBold(True)
        font4.setWeight(75)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"background-color:  None;\n"
"\n"
"\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 0, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(271, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)

        self.backbutton_3 = QPushButton(self.frame_2)
        self.backbutton_3.setObjectName(u"backbutton_3")
        self.backbutton_3.setMinimumSize(QSize(0, 40))
        self.backbutton_3.setMaximumSize(QSize(100, 16777215))
        self.backbutton_3.setFont(font1)
        self.backbutton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.backbutton_3.setStyleSheet(u"border-image: None;\n"
"background-color: rgb(30, 177, 167);")
        self.backbutton_3.setIcon(icon1)

        self.gridLayout_6.addWidget(self.backbutton_3, 0, 0, 1, 2)

        self.countries_button = QPushButton(self.frame_2)
        self.countries_button.setObjectName(u"countries_button")
        self.countries_button.setFont(font3)
        self.countries_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.countries_button.setStyleSheet(u"background-color: rgb(185, 44, 203);")

        self.gridLayout_6.addWidget(self.countries_button, 0, 4, 1, 1)


        self.gridLayout_4.addWidget(self.frame_2, 0, 1, 1, 1)

        self.views.addWidget(self.worldTour)

        self.gridLayout.addWidget(self.views, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
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
        self.backbutton_1.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"WELCOME TO TRAVEL ASSISTANT! \n"
"\n"
" We are so excited to help you choose the best option for your new adventure, but first you need to make the decision of how you wanna travel. \n"
"\n"
"  PERSONALIZED TRIP\n"
" If you travel with this option, you'll be able to choose a departure and arrival place. We'll make sure that you visit different countries and cultures on your way to your destination, while charging as little as possible :) \n"
"\n"
" ADVENTURE TRIP \n"
" With this option you'll be able to introduce your departure country and how much you want to spend in your trip, we'll give you a list of countries you can visit with said budget :)", None))
        self.personalized_button.setText(QCoreApplication.translate("MainWindow", u"PERSONALIZED TRIP", None))
        self.adventure_button.setText(QCoreApplication.translate("MainWindow", u"ADVENTURE TRIP", None))
        self.backbutton_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"First time traveling with us?", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_10.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Budget:", None))
        self.ready_button.setText(QCoreApplication.translate("MainWindow", u"Ready!", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"When you visit a country are you looking for...", None))
        self.star3_3.setText("")
        self.star2_2.setText("")
        self.star2_4.setText("")
        self.star1_3.setText("")
        self.star1_2.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Delicious food", None))
        self.star3_2.setText("")
        self.star1_1.setText("")
        self.star1_5.setText("")
        self.star1_4.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Good clothing stores", None))
        self.label_13.setText("")
        self.star2_5.setText("")
        self.star3_1.setText("")
        self.label_15.setText("")
        self.star2_1.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Great places to visit", None))
        self.star2_3.setText("")
        self.label_14.setText("")
        self.star3_4.setText("")
        self.star3_5.setText("")
        self.btnResetMap.setText(QCoreApplication.translate("MainWindow", u"Reset Map", None))
        self.groupBox.setTitle("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Departure:", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Arrival:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"WORLD TOUR", None))
        self.backbutton_3.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.countries_button.setText(QCoreApplication.translate("MainWindow", u"Countries", None))
    # retranslateUi

