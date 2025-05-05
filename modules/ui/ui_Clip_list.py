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
        Form.setStyleSheet(u"background-color: rgb(49,49,49);\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.framebar = QFrame(Form)
        self.framebar.setObjectName(u"framebar")
        self.framebar.setStyleSheet(u"background-color: #454545")
        self.framebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.framebar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.framebar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.framebar)
        self.title.setObjectName(u"title")

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.closeWindowButton = QPushButton(self.framebar)
        self.closeWindowButton.setObjectName(u"closeWindowButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.closeWindowButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.closeWindowButton)


        self.verticalLayout.addWidget(self.framebar)

        self.clipList = QScrollArea(Form)
        self.clipList.setObjectName(u"clipList")
        self.clipList.setStyleSheet(u"background-color: rgb(43, 43, 43);\n"
"border-radius: 12px;")
        self.clipList.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.clipList.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 783, 540))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.clip = QFrame(self.scrollAreaWidgetContents)
        self.clip.setObjectName(u"clip")
        self.clip.setMinimumSize(QSize(250, 175))
        self.clip.setMaximumSize(QSize(250, 175))
        self.clip.setStyleSheet(u"QFrame {\n"
"    background-color: #272727;\n"
"}\n"
"\n"
"#frame_2:hover {\n"
"    border: 2px solid #ffffff;\n"
"}")
        self.clip.setFrameShape(QFrame.Shape.StyledPanel)
        self.clip.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.clip)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.timestamp = QTextBrowser(self.clip)
        self.timestamp.setObjectName(u"timestamp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timestamp.sizePolicy().hasHeightForWidth())
        self.timestamp.setSizePolicy(sizePolicy)
        self.timestamp.setMinimumSize(QSize(0, 0))
        self.timestamp.setMaximumSize(QSize(150, 30))
        self.timestamp.setStyleSheet(u"background-color: #272727;\n"
"color: rgb(255,255,255);")

        self.gridLayout_2.addWidget(self.timestamp, 2, 0, 1, 1)

        self.image = QLabel(self.clip)
        self.image.setObjectName(u"image")
        self.image.setStyleSheet(u"background-color: #ffffff")
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.image, 0, 0, 2, 3)

        self.clipcheckBox = QCheckBox(self.clip)
        self.clipcheckBox.setObjectName(u"clipcheckBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clipcheckBox.sizePolicy().hasHeightForWidth())
        self.clipcheckBox.setSizePolicy(sizePolicy1)
        self.clipcheckBox.setMinimumSize(QSize(0, 0))
        self.clipcheckBox.setStyleSheet(u"")
        self.clipcheckBox.setCheckable(True)
        self.clipcheckBox.setTristate(False)

        self.gridLayout_2.addWidget(self.clipcheckBox, 2, 2, 1, 1)

        self.gridLayout_2.setRowStretch(0, 30)
        self.gridLayout_2.setColumnStretch(0, 110)

        self.gridLayout.addWidget(self.clip, 0, 0, 1, 1)

        self.clipList.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.clipList)

        self.downFrame = QHBoxLayout()
        self.downFrame.setObjectName(u"downFrame")
        self.downFrame.setContentsMargins(5, 5, 5, 5)
        self.clipCount = QLabel(Form)
        self.clipCount.setObjectName(u"clipCount")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.clipCount.sizePolicy().hasHeightForWidth())
        self.clipCount.setSizePolicy(sizePolicy2)

        self.downFrame.addWidget(self.clipCount)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.downFrame.addItem(self.horizontalSpacer)

        self.imageDownButoon = QPushButton(Form)
        self.imageDownButoon.setObjectName(u"imageDownButoon")

        self.downFrame.addWidget(self.imageDownButoon)

        self.textDownButton = QPushButton(Form)
        self.textDownButton.setObjectName(u"textDownButton")

        self.downFrame.addWidget(self.textDownButton)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.downFrame.addWidget(self.pushButton_3)


        self.verticalLayout.addLayout(self.downFrame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title.setText(QCoreApplication.translate("Form", u">>ViewAll", None))
        self.closeWindowButton.setText("")
        self.timestamp.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00:00:00 ~ 00:00:00</p></body></html>", None))
        self.image.setText(QCoreApplication.translate("Form", u"image", None))
        self.clipcheckBox.setText("")
        self.clipCount.setText(QCoreApplication.translate("Form", u"000/000", None))
        self.imageDownButoon.setText(QCoreApplication.translate("Form", u"Image", None))
        self.textDownButton.setText(QCoreApplication.translate("Form", u"Text", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Video", None))
    # retranslateUi

