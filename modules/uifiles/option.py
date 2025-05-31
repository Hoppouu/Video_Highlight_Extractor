import sys
from tokenize import Single
from PySide6.QtWidgets import QApplication, QDialog, QFileDialog
from PySide6.QtCore import Qt, Signal
from .ui_option import Ui_option_Form
from .dragger import WindowDragger

class UiOption(QDialog):
    optionApplied = Signal(str, int, int, int)
    changePath = Signal(bool)

    def __init__(self, path, startPoint, clipLength, skipFrame):
        super().__init__()
        self.ui = Ui_option_Form()
        self.ui.setupUi(self)
        
        self.playingPath = path
        self.path = path
        self.startPoint = startPoint
        self.clipLength = clipLength
        self.skipFrame = skipFrame

        #윈도우 프레임 제거
        self.setWindowFlag(Qt.FramelessWindowHint)

        # 닫기 버튼 연결
        self.ui.closeWindowButton.clicked.connect(self.close)
          
        #드래그 기능을 위한 WindowDragger 객체 생성
        self.dragger = WindowDragger(self.ui.framebar, self)

        self.ui.textEdit.setText(self.path)
        self.ui.spinBox.setValue(self.startPoint)
        self.ui.spinBox_2.setValue(self.clipLength)
        self.ui.spinBox_3.setValue(self.skipFrame)

        self.ui.pushButton.clicked.connect(self.emit_option)
        self.ui.pushButton_2.clicked.connect(self.load_play)

    def emit_option(self):
        # 현재 UI의 값을 원본 값에 저장
        self.path = self.ui.textEdit.text().strip()
        self.startPoint = self.ui.spinBox.value()
        self.clipLength = self.ui.spinBox_2.value()
        self.skipFrame = self.ui.spinBox_3.value()

        # 메인으로 적용된 값 보내기
        self.optionApplied.emit(
            self.path,
            self.startPoint,
            self.clipLength,
            self.skipFrame
        )

        self.changePath.emit(self.playingPath != self.path)
        self.playingPath = self.path

    def load_play(self):
        self.path, _ = QFileDialog.getOpenFileName(
            self, "영상 파일 선택", "", "Video Files (*.mp4 *.avi *.mkv)"
        )

        if self.path:
            self.ui.textEdit.setText(self.path)
        else:
            return