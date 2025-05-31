# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'optionQQjZEq.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTextEdit, QWidget)

class Ui_option_Form(object):
    def setupUi(self, option_Form):
        if not option_Form.objectName():
            option_Form.setObjectName(u"option_Form")
        option_Form.resize(400, 350)
        option_Form.setStyleSheet(u"background-color: #494949")
        self.gridLayout = QGridLayout(option_Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.label = QLabel(option_Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: #ffffff")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.textEdit = QLineEdit(option_Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMaxLength(600)
        self.textEdit.setMaximumSize(QSize(16777215, 30))
        self.textEdit.setStyleSheet(u"background-color: #ffffff")

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.pushButton_2 = QPushButton(option_Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: #ffffff")

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.horizontalLayout_3.setStretch(0, 70)
        self.horizontalLayout_3.setStretch(1, 300)
        self.horizontalLayout_3.setStretch(2, 30)

        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(option_Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"color: #ffffff")

        self.horizontalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)

        self.framebar = QFrame(option_Form)
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
        self.title.setStyleSheet(u"color : #ffffff")

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalSpacer_2 = QSpacerItem(764, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.closeWindowButton = QPushButton(self.framebar)
        self.closeWindowButton.setObjectName(u"closeWindowButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.closeWindowButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.closeWindowButton)


        self.gridLayout.addWidget(self.framebar, 0, 0, 1, 2)

        self.horizontalSpacer_3 = QSpacerItem(97, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 2, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setContentsMargins(10, 5, 0, -1)
        self.label_2 = QLabel(option_Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: #ffffff")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.spinBox = QSpinBox(option_Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFont(font)
        self.spinBox.setStyleSheet(u"color: #ffffff")
        self.spinBox.setMinimum(-180)
        self.spinBox.setMaximum(180)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.spinBox)

        self.label_3 = QLabel(option_Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: #ffffff")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.spinBox_2 = QSpinBox(option_Form)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setFont(font)
        self.spinBox_2.setStyleSheet(u"color: #ffffff")
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(180)
        self.spinBox_2.setValue(60)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.spinBox_2)

        self.label_4 = QLabel(option_Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: #ffffff")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.spinBox_3 = QSpinBox(option_Form)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setStyleSheet(u"color: #ffffff")
        self.spinBox_3.setMaximum(60)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.spinBox_3)


        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 24)
        self.gridLayout.setRowStretch(1, 24)
        self.gridLayout.setRowStretch(2, 268)
        self.gridLayout.setRowStretch(3, 24)
        self.gridLayout.setColumnStretch(0, 150)
        self.gridLayout.setColumnStretch(1, 50)

        self.retranslateUi(option_Form)

        QMetaObject.connectSlotsByName(option_Form)
    # setupUi

    def retranslateUi(self, option_Form):
        option_Form.setWindowTitle(QCoreApplication.translate("option_Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("option_Form", u"\uc601\uc0c1 \uc8fc\uc18c", None))
        self.pushButton_2.setText(QCoreApplication.translate("option_Form", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("option_Form", u"\uc801\uc6a9", None))
        self.title.setText(QCoreApplication.translate("option_Form", u">>Option", None))
        self.closeWindowButton.setText("")
        self.label_2.setText(QCoreApplication.translate("option_Form", u"\uc2dc\uc791\uc9c0\uc810", None))
        self.label_3.setText(QCoreApplication.translate("option_Form", u"\ucd94\ucd9c \uae38\uc774", None))
        self.label_4.setText(QCoreApplication.translate("option_Form", u"\uc774\ub3d9 \ud504\ub808\uc784", None))
    # retranslateUi

