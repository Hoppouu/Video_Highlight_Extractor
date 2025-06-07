import os
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QCheckBox, QPushButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Signal

from modules import constants
from modules.uifiles.clip_maker import ThumbnailMaker

class ClipWidget(QWidget):
    # 시작 및 끝 시간을 전달하는 신호 정의
    time_selected = Signal(str)

    def __init__(self, video_path, fps, start_time, end_time, description="", show_description=True,thumbnail_index=0, parent=None):
        super().__init__(parent)
        self.start_time = start_time
        self.end_time = end_time
        #self.setFixedSize(250, 175)  # 위젯 크기 설정
        self.setStyleSheet("background-color: #272727; border-radius: 8px;")

# ================================================================
        self.thumbnail_label = QLabel(self)

        current_dir = constants.file_path_images #파일 경로
        thumbnail_path = os.path.join(current_dir, f"{thumbnail_index}.jpg")

        if os.path.exists(thumbnail_path):
            pixmap = QPixmap(thumbnail_path)
        else:
            # 대체 이미지 경로
            fallback_path = os.path.join(current_dir, "none_image.png")
            pixmap = QPixmap(fallback_path) if os.path.exists(fallback_path) else QPixmap()

        # # 썸네일 이미지
        # self.thumbnail_label = QLabel(self)
        # pixmap = ThumbnailMaker.from_video(video_path, fps, start_time)

        # if not pixmap:
        #     # 현재 파일의 경로를 기준으로 상대 경로 설정
        #     current_dir = os.path.dirname(__file__)
        #     fallback_path = os.path.join(current_dir, "none_image.png")

        #     if os.path.exists(fallback_path):
        #         pixmap = QPixmap(fallback_path)
        #     else:
        #         pixmap = QPixmap()  # or 빈 픽스맵으로 예외 방지

        self.thumbnail_label.setPixmap(pixmap.scaled(230, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.thumbnail_label.setAlignment(Qt.AlignCenter)
        self.thumbnail_label.setStyleSheet("background-color: #3a3a3a; border-radius: 6px;")  # 밝은 회색 배경 추가

        # 설명 텍스트
        self.desc_label = QLabel(description, self)
        self.desc_label.setStyleSheet("color: #bbb; font-size: 11px; margin: 2px 0 2px 0;")
        self.desc_label.setWordWrap(True)
        self.desc_label.setVisible(show_description)  # << 여기!

        # 시작 시간 버튼
        self.start_button = QPushButton(start_time, self)
        self.start_button.setStyleSheet("color: white; font-size: 12px; background-color: #444; border: none;")
        self.start_button.clicked.connect(lambda: self.time_selected.emit(self.start_time))

        # 끝 시간 버튼
        self.end_button = QPushButton(end_time, self)
        self.end_button.setStyleSheet("color: white; font-size: 12px; background-color: #444; border: none;")
        self.end_button.clicked.connect(lambda: self.time_selected.emit(self.end_time))

        # 체크박스
        self.checkbox = QCheckBox(self)
        self.checkbox.setStyleSheet("margin-left: 10px;")

        # 하단 영역 (시작 버튼 + 끝 버튼 + 체크박스)
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.start_button)
        bottom_layout.addWidget(self.end_button)
        bottom_layout.addStretch()
        bottom_layout.addWidget(self.checkbox)

        # 전체 레이아웃
        layout = QVBoxLayout(self)
        layout.addWidget(self.thumbnail_label, 6)
        if show_description:
            layout.addWidget(self.desc_label, 1)
        layout.addLayout(bottom_layout)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        self.setLayout(layout)

    # ClipWidget 내부 (썸네일 QLabel이 self.thumbnail_label이라고 가정)
    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, "thumbnail_pixmap") and self.thumbnail_pixmap:
            self.thumbnail_label.setPixmap(
                self.thumbnail_pixmap.scaled(
                    self.thumbnail_label.width(),
                    self.thumbnail_label.height(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )