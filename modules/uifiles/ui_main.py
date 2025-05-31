# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RereuizFFaKI.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QTextBrowser, QVBoxLayout, QWidget)
from PySide6.QtMultimediaWidgets import QVideoWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1273, 760)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 0, 0)
        self.framebar = QFrame(self.centralwidget)
        self.framebar.setObjectName(u"framebar")
        self.framebar.setMinimumSize(QSize(0, 30))
        self.framebar.setAutoFillBackground(False)
        self.framebar.setStyleSheet(u"background-color: rgb(61, 61, 61);")
        self.framebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.framebar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.framebar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.framebar)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setStyleSheet(u"color: #ffffff;")

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.minimizeWindow = QPushButton(self.framebar)
        self.minimizeWindow.setObjectName(u"minimizeWindow")
        self.minimizeWindow.setMinimumSize(QSize(30, 30))
        self.minimizeWindow.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;\n"
"    color: white;\n"
"    border: 2px solid #595959;\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        #self.minimizeWindow.setIcon(icon)
        self.minimizeWindow.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.minimizeWindow)

        self.toggleMaximizeRestore = QPushButton(self.framebar)
        self.toggleMaximizeRestore.setObjectName(u"toggleMaximizeRestore")
        self.toggleMaximizeRestore.setMinimumSize(QSize(30, 30))
        self.toggleMaximizeRestore.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;\n"
"    color: white;\n"
"    border: 2px solid #595959;\n"
"}")
        #self.toggleMaximizeRestore.setIcon(icon)
        self.toggleMaximizeRestore.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.toggleMaximizeRestore)

        self.closeWindow = QPushButton(self.framebar)
        self.closeWindow.setObjectName(u"closeWindow")
        self.closeWindow.setMinimumSize(QSize(30, 30))
        self.closeWindow.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;\n"
"    color: white;\n"
"    border: 2px solid #595959;\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        #self.closeWindow.setIcon(icon1)
        self.closeWindow.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.closeWindow)

        self.horizontalLayout.setStretch(0, 100)
        self.horizontalLayout.setStretch(1, 1083)
        self.horizontalLayout.setStretch(2, 30)
        self.horizontalLayout.setStretch(3, 30)
        self.horizontalLayout.setStretch(4, 30)

        self.verticalLayout.addWidget(self.framebar)

        self.mainFrame = QGridLayout()
        self.mainFrame.setSpacing(0)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setContentsMargins(7, 5, 7, 10)
        self.videoPlayer = QLabel(self.centralwidget)
        self.videoPlayer.setObjectName(u"videoPlayer")
        self.videoPlayer.setStyleSheet(u"border: 3px dashed #414141;")

        self.mainFrame.addWidget(self.videoPlayer, 0, 0, 1, 1)

        self.clipList = QScrollArea(self.centralwidget)
        self.clipList.setObjectName(u"clipList")
        self.clipList.setMinimumSize(QSize(240, 681))
        self.clipList.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"border-radius: 12px;")
        self.clipList.setFrameShape(QFrame.Shape.NoFrame)
        self.clipList.setFrameShadow(QFrame.Shadow.Sunken)
        self.clipList.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.clipList.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 241, 681))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 0)

        # 예시 클립 제거됨

        self.clipList.setWidget(self.scrollAreaWidgetContents)

        #self.mainFrame.addWidget(self.clipList, 0, 1, 3, 1, Qt.AlignmentFlag.AlignTop)
        self.mainFrame.addWidget(self.clipList, 0, 1, 3, 1)


        self.playSlider = QSlider(self.centralwidget)
        self.playSlider.setObjectName(u"playSlider")
        self.playSlider.setMaximum(1000)
        self.playSlider.setOrientation(Qt.Orientation.Horizontal)

        self.mainFrame.addWidget(self.playSlider, 1, 0, 1, 1)

        self.playbackFrame = QHBoxLayout()
        self.playbackFrame.setSpacing(0)
        self.playbackFrame.setObjectName(u"playbackFrame")
        self.videoTime = QLabel(self.centralwidget)
        self.videoTime.setObjectName(u"videoTime")
        font1 = QFont()
        font1.setPointSize(13)
        self.videoTime.setFont(font1)
        self.videoTime.setStyleSheet(u"color: rgb(180, 180, 180);")
        self.videoTime.setFrameShape(QFrame.Shape.Box)
        self.videoTime.setLineWidth(1)
        self.videoTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.videoTime.setIndent(-1)

        self.playbackFrame.addWidget(self.videoTime)

        self.playSpeedDoubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.playSpeedDoubleSpinBox.setObjectName(u"playSpeedDoubleSpinBox")
        self.playSpeedDoubleSpinBox.setStyleSheet(u"color: rgb(180, 180, 180);")
        self.playSpeedDoubleSpinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.playSpeedDoubleSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.playSpeedDoubleSpinBox.setMinimum(0.2500000000000000)
        self.playSpeedDoubleSpinBox.setMaximum(2.000000000000000)
        self.playSpeedDoubleSpinBox.setSingleStep(0.250000000000000)
        self.playSpeedDoubleSpinBox.setValue(1.000000000000000)
        self.playSpeedDoubleSpinBox.lineEdit().setReadOnly(True)

        self.playbackFrame.addWidget(self.playSpeedDoubleSpinBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.playbackFrame.addItem(self.horizontalSpacer_3)

        self.playbackFrame.setStretch(0, 90)
        self.playbackFrame.setStretch(1, 10)
        self.playbackFrame.setStretch(2, 9400)

        self.mainFrame.addLayout(self.playbackFrame, 2, 0, 1, 1)

        self.playFrame = QHBoxLayout()
        self.playFrame.setSpacing(1)
        self.playFrame.setObjectName(u"playFrame")
        self.slowDownButton = QPushButton(self.centralwidget)
        self.slowDownButton.setObjectName(u"slowDownButton")
        self.slowDownButton.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.slowDownButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(41, 41, 41);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;\n"
"    color: white;  \n"
"    border: 2px solid #595959; \n"
"}")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekBackward))
        self.slowDownButton.setIcon(icon2)
        self.slowDownButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.slowDownButton)

        self.skipBackwardButton = QPushButton(self.centralwidget)
        self.skipBackwardButton.setObjectName(u"skipBackwardButton")
        self.skipBackwardButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(41, 41, 41);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;\n"
"    color: white;  \n"
"    border: 2px solid #595959; \n"
"}")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipBackward))
        self.skipBackwardButton.setIcon(icon3)
        self.skipBackwardButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.skipBackwardButton)

        self.playVideoButton = QPushButton(self.centralwidget)
        self.playVideoButton.setObjectName(u"playVideoButton")
        self.playVideoButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(41, 41, 41);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;\n"
"    color: white;  \n"
"    border: 2px solid #595959; \n"
"}")
        self.icon_play = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))
        self.icon_pause = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.playVideoButton.setIcon(self.icon_pause) 
        self.playVideoButton.setIconSize(QSize(30, 30))
        self.playVideoButton.setMinimumSize(40, 40)   # 아이콘 크기
        self.playVideoButton.setMaximumSize(40, 40)   # 아이콘 크기

        self.playFrame.addWidget(self.playVideoButton)

        self.skipForwardButton = QPushButton(self.centralwidget)
        self.skipForwardButton.setObjectName(u"skipForwardButton")
        self.skipForwardButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(41, 41, 41);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;\n"
"    color: white;  \n"
"    border: 2px solid #595959; \n"
"}")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward))
        self.skipForwardButton.setIcon(icon5)
        self.skipForwardButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.skipForwardButton)

        self.speedUpButton = QPushButton(self.centralwidget)
        self.speedUpButton.setObjectName(u"speedUpButton")
        self.speedUpButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(41, 41, 41);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;\n"
"    color: white;  \n"
"    border: 2px solid #595959; \n"
"}")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.speedUpButton.setIcon(icon6)
        self.speedUpButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.speedUpButton)

        self.toggleMuteButton = QPushButton(self.centralwidget)
        self.toggleMuteButton.setObjectName(u"toggleMuteButton")
        self.toggleMuteButton.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	background-color: rgb(41, 41, 41);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;\n"
"    color: white;  \n"
"    border: 2px solid #595959; \n"
"}")
        icon7 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AudioVolumeHigh))
        self.toggleMuteButton.setIcon(icon7)
        self.toggleMuteButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.toggleMuteButton)

        self.volumeBar = QSlider(self.centralwidget)
        self.volumeBar.setObjectName(u"volumeBar")
        self.volumeBar.setMaximum(100)
        self.volumeBar.setPageStep(1)
        self.volumeBar.setValue(100)
        self.volumeBar.setTracking(True)
        self.volumeBar.setOrientation(Qt.Orientation.Horizontal)
        self.volumeBar.setTickPosition(QSlider.TickPosition.NoTicks)

        self.playFrame.addWidget(self.volumeBar)

        self.volumeSpinBox = QSpinBox(self.centralwidget)
        self.volumeSpinBox.setObjectName(u"volumeSpinBox")
        self.volumeSpinBox.setStyleSheet(u"color: rgb(180, 180, 180);")
        self.volumeSpinBox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.volumeSpinBox.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.volumeSpinBox.setMaximum(100)
        self.volumeSpinBox.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.volumeSpinBox.setValue(100)

        self.playFrame.addWidget(self.volumeSpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.playFrame.addItem(self.horizontalSpacer_2)

        self.optionButton = QPushButton(self.centralwidget)
        self.optionButton.setObjectName(u"optionButton")
        self.optionButton.setStyleSheet(u"color: #aaaaaa")

        self.playFrame.addWidget(self.optionButton)

        self.playFrame.setStretch(0, 30)
        self.playFrame.setStretch(1, 30)
        self.playFrame.setStretch(2, 30)
        self.playFrame.setStretch(3, 30)
        self.playFrame.setStretch(4, 30)
        self.playFrame.setStretch(5, 30)
        self.playFrame.setStretch(6, 120)
        self.playFrame.setStretch(7, 10)
        self.playFrame.setStretch(8, 730)

        self.mainFrame.addLayout(self.playFrame, 3, 0, 1, 1)

        self.viewClipButton = QPushButton(self.centralwidget)
        self.viewClipButton.setObjectName(u"viewClipButton")
        icon8 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.viewClipButton.setIcon(icon8)

        self.mainFrame.addWidget(self.viewClipButton, 3, 1, 1, 1)

        self.mainFrame.setRowStretch(0, 567)
        self.mainFrame.setRowStretch(1, 30)
        self.mainFrame.setRowStretch(2, 20)
        self.mainFrame.setRowStretch(3, 30)
        self.mainFrame.setColumnStretch(0, 1008)
        self.mainFrame.setColumnStretch(1, 240)

        self.verticalLayout.addLayout(self.mainFrame)

        self.verticalLayout.setStretch(0, 20)
        self.verticalLayout.setStretch(1, 740)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.volumeBar.sliderMoved.connect(self.volumeSpinBox.setValue)
        self.volumeSpinBox.valueChanged.connect(self.volumeBar.setValue)
        self.speedUpButton.clicked.connect(self.playSpeedDoubleSpinBox.stepUp)
        self.slowDownButton.clicked.connect(self.playSpeedDoubleSpinBox.stepDown)

        self.minimizeWindow.setText("—")
        self.toggleMaximizeRestore.setText("□")
        self.closeWindow.setText("×")

        self.minimizeWindow.setStyleSheet("""
        QPushButton { 
                color: white; 
                border: none; 
                background: transparent; 
                font-size: 16px;
        }
        QPushButton:hover { background: #e0e0e0; color: black; }
        """)
        self.toggleMaximizeRestore.setStyleSheet("""
        QPushButton { 
                color: white; 
                border: none; 
                background: transparent; 
                font-size: 14px;
        }
        QPushButton:hover { background: #e0e0e0; color: black; }
        """)
        self.closeWindow.setStyleSheet("""
        QPushButton { 
                color: white; 
                border: none; 
                background: transparent; 
                font-size: 20px;
        }
        QPushButton:hover { background: #e57373; color: black; }
        """)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"HighLight", None))
        self.minimizeWindow.setText("")
        self.toggleMaximizeRestore.setText("")
        self.closeWindow.setText("")
        self.videoTime.setText(QCoreApplication.translate("MainWindow", u"00:00:00 / 00:00:00", None))
        self.viewClipButton.setText("")
        self.slowDownButton.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
        self.skipBackwardButton.setShortcut(QCoreApplication.translate("MainWindow", u"Z", None))
        self.playVideoButton.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
        self.skipForwardButton.setShortcut(QCoreApplication.translate("MainWindow", u"X", None))
        self.speedUpButton.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
        self.toggleMuteButton.setShortcut(QCoreApplication.translate("MainWindow", u"M", None))
        self.optionButton.setText(QCoreApplication.translate("MainWindow", u"Option", None))
    # retranslateUi