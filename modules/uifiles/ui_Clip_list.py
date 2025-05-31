# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clip_listZtXCAN.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        Form.setMinimumSize(QSize(800, 600))
        Form.setMaximumSize(QSize(800, 600))
        Form.setStyleSheet(u"background-color: rgb(49,49,49);")

        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        # 상단 바
        self.framebar = QFrame(Form)
        self.framebar.setObjectName(u"framebar")
        self.framebar.setStyleSheet(u"background-color: #454545")
        self.framebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.framebar.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2 = QHBoxLayout(self.framebar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.title = QLabel(self.framebar)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: #ffffff;")
        self.title.setObjectName(u"title")

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.closeWindowButton = QPushButton(self.framebar)
        self.closeWindowButton.setObjectName(u"closeWindowButton")
        self.closeWindowButton.setText("×")
        self.closeWindowButton.setStyleSheet("""
            QPushButton { 
                color: white; 
                border: none; 
                background: transparent; 
                font-size: 20px;
            }
            QPushButton:hover { background: #e57373; color: black; }
        """)
        self.closeWindowButton.setMinimumSize(30, 30)
        self.closeWindowButton.setMaximumSize(30, 30)
        self.closeWindowButton.setIcon(QIcon())

        self.horizontalLayout_2.addWidget(self.closeWindowButton)
        self.verticalLayout.addWidget(self.framebar)

    

        # 클립 리스트
        self.clipList = QScrollArea(Form)
        self.clipList.setObjectName(u"clipList")
        self.clipList.setStyleSheet(u"background-color: rgb(43, 43, 43);\nborder-radius: 12px;")
        self.clipList.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.clipList.setWidgetResizable(True)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 783, 540))

        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")

        self.clipList.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.clipList)

        # 하단 버튼 영역
        self.downFrame = QHBoxLayout()
        self.downFrame.setObjectName(u"downFrame")
        self.downFrame.setContentsMargins(5, 5, 5, 5)

        self.clipCount = QLabel(Form)
        self.clipCount.setObjectName(u"clipCount")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.clipCount.setSizePolicy(sizePolicy)
        self.downFrame.addWidget(self.clipCount)
        self.clipCount.setStyleSheet(u"color: #cccccc")

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.downFrame.addItem(self.horizontalSpacer)

        self.imageDownButoon = QPushButton(Form)
        self.imageDownButoon.setObjectName(u"imageDownButoon")
        self.downFrame.addWidget(self.imageDownButoon)
        self.imageDownButoon.setStyleSheet(u"color: #cccccc")

        self.textDownButton = QPushButton(Form)
        self.textDownButton.setObjectName(u"textDownButton")
        self.downFrame.addWidget(self.textDownButton)
        self.textDownButton.setStyleSheet(u"color: #cccccc")

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.downFrame.addWidget(self.pushButton_3)
        self.pushButton_3.setStyleSheet(u"color: #cccccc")

        self.verticalLayout.addLayout(self.downFrame)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u">>ViewAll", None))
        #self.closeWindowButton.setText("")
        self.clipCount.setText(QCoreApplication.translate("Form", u"000/000", None))
        self.imageDownButoon.setText(QCoreApplication.translate("Form", u"Image", None))
        self.textDownButton.setText(QCoreApplication.translate("Form", u"Text", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Video", None))

