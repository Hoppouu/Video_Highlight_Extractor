from PySide6.QtWidgets import QDialog, QFileDialog, QFrame, QLabel, QVBoxLayout, QCheckBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from .ClipWidget import ClipWidget  # ClipWidget 클래스 임포트
from .ui_Clip_list import Ui_Form
from PySide6.QtCore import Qt, QObject, QEvent
from PySide6.QtCore import Signal
from .ClipWidget import ClipWidget
from .dragger import WindowDragger
from modules.uifiles.utils import time_to_sec, sec_to_time
from modules.uifiles.option import UiOption

class UiForm(QDialog):
    checkbox_changed = Signal(tuple, bool)  # (key, state)
    makeclip = Signal(bool, str)
    def __init__(self, timeline_data, check_state, player, clipLength, path, fps, videoLength, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.player = player #타임라인 적용을 위한 player 저장
        self.check_state = check_state
        self.clip_widgets = []
        self.clipLength = clipLength  # 추가
        self.path = path
        self.fps = fps
        self.videoLength = videoLength
        self.populate_clip_list(timeline_data)


        #윈도우 프레임 제거
        self.setWindowFlag(Qt.FramelessWindowHint)

        # 닫기 버튼 연결
        self.ui.closeWindowButton.clicked.connect(self.close)
          
        #드래그 기능을 위한 WindowDragger 객체 생성
        self.dragger = WindowDragger(self.ui.framebar, self)

        #다운 버튼 연결 *video만 연결함
        self.ui.pushButton_3.clicked.connect(self.emit_button)

        #클립 개수
        self.update_clip_count_label()

    def populate_clip_list(self, timeline_data):
        columns = 3
        index = 0
        # 동영상이 로드되지 않았으면 클립 생성하지 않음
        if not self.player or self.player.get_length() <= 0:
            return

        for index, clip in enumerate(timeline_data):
            start_sec = time_to_sec(clip["start_time"])
            end_sec = start_sec + self.clipLength
            self.end_time = sec_to_time(min(self.videoLength, end_sec))
            key = (clip["start_time"], self.end_time)
            clip_widget = ClipWidget(
                video_path=self.path,
                fps=self.fps,
                start_time=clip["start_time"],
                end_time=self.end_time,
                show_description=False,
                # =========================
                thumbnail_index = index
            )
            clip_widget.time_selected.connect(self.seek_video_to_time)
            clip_widget.checkbox.setChecked(self.check_state.get(key[0], False))
            clip_widget.checkbox.stateChanged.connect(lambda state, k=key: self.checkbox_changed.emit(k, state))
            self.clip_widgets.append(clip_widget)
            row = index // columns
            column = index % columns
            self.ui.gridLayout.addWidget(clip_widget, row, column)
            index = index + 1

    def update_checkbox_state(self, key, state):
        for w in self.clip_widgets:
            if w.start_time == key[0]:
                w.checkbox.setChecked(state)

        self.update_clip_count_label()

    
    def seek_video_to_time(self, time_str):
        h, m, s = map(int, time_str.split(":"))
        ms = (h * 3600 + m * 60 + s) * 1000
        self.player.set_time(ms)

    def emit_button(self):
        if self.load_play():
            self.makeclip.emit(True, self.out_path)

    def load_play(self):
        folder_path = QFileDialog.getExistingDirectory(
            self, "저장할 폴더 선택", ""
        )
        if folder_path:
            self.out_path = folder_path
            return True
        return False

    def update_clip_count_label(self):
        total = len(self.check_state)
        checked = sum(1 for checked in self.check_state.values() if checked)
        self.ui.clipCount.setText(f"{checked} / {total}")

    