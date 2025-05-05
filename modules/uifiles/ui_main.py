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
        palette = QPalette()
        brush = QBrush(QColor(61, 61, 61, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.minimizeWindow.setPalette(palette)
        self.minimizeWindow.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #494949;  /* \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c \ubc30\uacbd \uc0c9\uc0c1 */\n"
"    color: white;  /* \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 */\n"
"    border: 2px solid #595959;  /* \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c \ud14c\ub450\ub9ac \uc0c9\uc0c1 */\n"
"}")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ApplicationExit))
        self.minimizeWindow.setIcon(icon)
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
"    background-color: #494949;  /* \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c \ubc30\uacbd \uc0c9\uc0c1 */\n"
"    color: white;  /* \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 */\n"
"    border: 2px solid #595959;  /* \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c \ud14c\ub450\ub9ac \uc0c9\uc0c1 */\n"
"}")
        self.toggleMaximizeRestore.setIcon(icon)
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
"    background-color: #494949;  /* \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c \ubc30\uacbd \uc0c9\uc0c1 */\n"
"    color: white;  /* \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 */\n"
"    border: 2px solid #595959;  /* \ub9c8\uc6b0\uc2a4\ub97c \uc62c\ub838\uc744 \ub54c \ud14c\ub450\ub9ac \uc0c9\uc0c1 */\n"
"}")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.WindowClose))
        self.closeWindow.setIcon(icon1)
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
        self.videoPlayer = QWidget(self.centralwidget)
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
        self.clip = QFrame(self.scrollAreaWidgetContents)
        self.clip.setObjectName(u"clip")
        self.clip.setMinimumSize(QSize(220, 150))
        self.clip.setMaximumSize(QSize(220, 150))
        self.clip.setStyleSheet(u"background-color: rgb(39, 39, 39);")
        self.clip.setFrameShape(QFrame.Shape.StyledPanel)
        self.clip.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.clip)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 5, 0, 5)
        self.timestamp = QTextBrowser(self.clip)
        self.timestamp.setObjectName(u"timestamp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timestamp.sizePolicy().hasHeightForWidth())
        self.timestamp.setSizePolicy(sizePolicy)
        self.timestamp.setMaximumSize(QSize(150, 30))
        self.timestamp.setStyleSheet(u"background-color: rgb(39, 39, 39);\n"
"color: rgb(255,255,255);")

        self.gridLayout_9.addWidget(self.timestamp, 0, 0, 1, 1)

        self.clipCheckBox = QCheckBox(self.clip)
        self.clipCheckBox.setObjectName(u"clipCheckBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clipCheckBox.sizePolicy().hasHeightForWidth())
        self.clipCheckBox.setSizePolicy(sizePolicy1)
        self.clipCheckBox.setStyleSheet(u"")
        self.clipCheckBox.setCheckable(True)

        self.gridLayout_9.addWidget(self.clipCheckBox, 0, 1, 1, 1)

        self.downButton = QPushButton(self.clip)
        self.downButton.setObjectName(u"downButton")
        sizePolicy1.setHeightForWidth(self.downButton.sizePolicy().hasHeightForWidth())
        self.downButton.setSizePolicy(sizePolicy1)
        self.downButton.setSizeIncrement(QSize(0, 0))
        self.downButton.setBaseSize(QSize(0, 0))
        self.downButton.setStyleSheet(u"QPushButton {\n"
"	border: 1px solid block;\n"
"	color: rgb(255,255,255);\n"
"}")

        self.gridLayout_9.addWidget(self.downButton, 0, 2, 1, 1)

        self.summary = QLabel(self.clip)
        self.summary.setObjectName(u"summary")
        sizePolicy.setHeightForWidth(self.summary.sizePolicy().hasHeightForWidth())
        self.summary.setSizePolicy(sizePolicy)
        self.summary.setStyleSheet(u"background-color: rgb(70, 70, 70);\n"
"border-radius: 0;\n"
"color: rgb(255,255,255);")
        self.summary.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_9.addWidget(self.summary, 1, 0, 1, 3)

        self.gridLayout_9.setRowStretch(0, 30)
        self.gridLayout_9.setRowStretch(1, 220)
        self.gridLayout_9.setColumnStretch(0, 110)
        self.gridLayout_9.setColumnStretch(1, 55)
        self.gridLayout_9.setColumnStretch(2, 55)

        self.verticalLayout_2.addWidget(self.clip)

        self.clipList.setWidget(self.scrollAreaWidgetContents)

        self.mainFrame.addWidget(self.clipList, 0, 1, 3, 1, Qt.AlignmentFlag.AlignTop)

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
        self.playSpeedDoubleSpinBox.setMinimum(-2.000000000000000)
        self.playSpeedDoubleSpinBox.setMaximum(2.000000000000000)
        self.playSpeedDoubleSpinBox.setSingleStep(0.250000000000000)
        self.playSpeedDoubleSpinBox.setValue(1.000000000000000)

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
        self.slowDownButton.setStyleSheet(u"background-color: rgb(41, 41, 41);\n"
"border-radius: 3px;")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekBackward))
        self.slowDownButton.setIcon(icon2)
        self.slowDownButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.slowDownButton)

        self.skipBackwardButton = QPushButton(self.centralwidget)
        self.skipBackwardButton.setObjectName(u"skipBackwardButton")
        self.skipBackwardButton.setStyleSheet(u"background-color: rgb(41, 41, 41);\n"
"border-radius: 3px;")
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipBackward))
        self.skipBackwardButton.setIcon(icon3)
        self.skipBackwardButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.skipBackwardButton)

        self.playVideoButton = QPushButton(self.centralwidget)
        self.playVideoButton.setObjectName(u"playVideoButton")
        self.playVideoButton.setStyleSheet(u"background-color: rgb(41, 41, 41);\n"
"border-radius: 3px;")
        icon4 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
        self.playVideoButton.setIcon(icon4)
        self.playVideoButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.playVideoButton)

        self.skipForwardButton = QPushButton(self.centralwidget)
        self.skipForwardButton.setObjectName(u"skipForwardButton")
        self.skipForwardButton.setStyleSheet(u"background-color: rgb(41, 41, 41);\n"
"border-radius: 3px;")
        icon5 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSkipForward))
        self.skipForwardButton.setIcon(icon5)
        self.skipForwardButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.skipForwardButton)

        self.speedUpButton = QPushButton(self.centralwidget)
        self.speedUpButton.setObjectName(u"speedUpButton")
        self.speedUpButton.setStyleSheet(u"background-color: rgb(41, 41, 41);\n"
"border-radius: 3px;")
        icon6 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekForward))
        self.speedUpButton.setIcon(icon6)
        self.speedUpButton.setIconSize(QSize(30, 30))

        self.playFrame.addWidget(self.speedUpButton)

        self.toggleMuteButton = QPushButton(self.centralwidget)
        self.toggleMuteButton.setObjectName(u"toggleMuteButton")
        self.toggleMuteButton.setStyleSheet(u"background-color: rgb(41, 41, 41);\n"
"border-radius: 3px;")
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

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"HighLight", None))
        self.minimizeWindow.setText("")
        self.toggleMaximizeRestore.setText("")
        self.closeWindow.setText("")
        self.timestamp.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\ub9d1\uc740 \uace0\ub515'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00:00:00 ~ 00:00:00</p></body></html>", None))
        self.clipCheckBox.setText("")
        self.downButton.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.summary.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.videoTime.setText(QCoreApplication.translate("MainWindow", u"00:00:00 / 00:00:00", None))
        self.slowDownButton.setText("")
#if QT_CONFIG(shortcut)
        self.slowDownButton.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.skipBackwardButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>SkipBackward</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.skipBackwardButton.setText("")
#if QT_CONFIG(shortcut)
        self.skipBackwardButton.setShortcut(QCoreApplication.translate("MainWindow", u"Z", None))
#endif // QT_CONFIG(shortcut)
        self.playVideoButton.setText("")
#if QT_CONFIG(shortcut)
        self.playVideoButton.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(whatsthis)
        self.skipForwardButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>MediaSkipForward</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.skipForwardButton.setText("")
#if QT_CONFIG(shortcut)
        self.skipForwardButton.setShortcut(QCoreApplication.translate("MainWindow", u"X", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.speedUpButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.speedUpButton.setText("")
#if QT_CONFIG(shortcut)
        self.speedUpButton.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(whatsthis)
        self.toggleMuteButton.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>MediaSkipForward</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toggleMuteButton.setText("")
#if QT_CONFIG(shortcut)
        self.toggleMuteButton.setShortcut(QCoreApplication.translate("MainWindow", u"M", None))
#endif // QT_CONFIG(shortcut)
        self.viewClipButton.setText("")
    # retranslateUi

