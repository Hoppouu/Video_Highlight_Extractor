# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'massitbLxP.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 200)
        Form.setStyleSheet(u"background-color: #494949")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(5)
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
        self.horizontalSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.closeWindowButton = QPushButton(self.framebar)
        self.closeWindowButton.setObjectName(u"closeWindowButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.closeWindowButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.closeWindowButton)


        self.verticalLayout.addWidget(self.framebar)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #ffffff")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setMargin(5)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: #ffffff")

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 24)
        self.verticalLayout.setStretch(1, 152)
        self.verticalLayout.setStretch(2, 24)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.closeWindowButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\uc801\uc6a9", None))
    # retranslateUi

