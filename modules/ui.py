import os
import zipfile
import ctypes
import sys
import cv2

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QSlider, QSizePolicy
from PySide6.QtCore import Qt, QObject, QEvent, QTimer, Signal
from modules import utils, assemble
# 프로젝트 루트(두 단계의 상위 폴더)의 절대 경로를 sys.path 최상단에 추가
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from modules.uifiles.ClipWidget import ClipWidget
from modules.uifiles.ui_main import Ui_MainWindow
from modules.uifiles.option import UiOption
from modules.uifiles.viewall import UiForm
from modules.uifiles.dragger import WindowDragger
from modules.uifiles.clip_maker import ClipMaker
from modules.uifiles.utils import time_to_sec, sec_to_time

# 압축 파일 경로
ZIP_PATH = os.path.join(os.path.dirname(__file__), "uifiles", "vlc_package.zip")
EXTRACT_DIR = os.path.join(os.path.dirname(__file__), "uifiles", "vlc_runtime")

def setup_vlc_environment():
    # vlc_runtime 디렉토리가 없으면 압축 해제
    if not os.path.exists(EXTRACT_DIR):
        with zipfile.ZipFile(ZIP_PATH, 'r') as zip_ref:
            zip_ref.extractall(EXTRACT_DIR)
    
    dll_dir = os.path.join(EXTRACT_DIR, "vlc_package")
    if hasattr(os, "add_dll_directory"):
        os.add_dll_directory(dll_dir)

    os.environ["PATH"] = dll_dir + os.pathsep + os.environ.get("PATH", "")
    
    libvlc_path = os.path.join(dll_dir, "libvlc.dll")
    ctypes.CDLL(libvlc_path)
    
    return dll_dir

vlc_base_path = setup_vlc_environment()

import vlc

file_path_origin = "./result/"
file_path_subtitle = file_path_origin + "subtitles/"
file_path_llm_outputs = file_path_origin + "llm_outputs/"
llm_output = file_path_llm_outputs + "abc.txt"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    
        # 옵션 기본 값
        self.path = None    # 영상 주소
        self.startPoint = -30 # 클립 시작 위치, 받은 결과에서 사용자가 조절용
        self.clipLength = 60    # 클립 길이
        self.skipFrame = 3  # 움직일 프레임 크기
    
        # 타임라인 데이터 예시
        self.timeline_data = utils.dic_to_ui_dic(llm_output)

        #영상 출력 핸들러
        self.video_hander = VideoPlayerHandler(self, self.ui, self.path, self.skipFrame)
        self.ui.videoPlayer.mousePressEvent = self.on_video_click
        self.video_hander.load_video.connect(self.on_load_video)

        # 체크 상태를 저장할 딕셔너리 (key: (start, end), value: bool)
        self.clip_check_state = {}
        for clip in self.timeline_data:
            key = (clip["start_time"])
            self.clip_check_state[key] = False

        #윈도우 프레임 제거
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        #윈도우 프레임 조작
        self.ui.closeWindow.clicked.connect(QApplication.quit)
        self.ui.minimizeWindow.clicked.connect(self.showMinimized)
        self.ui.toggleMaximizeRestore.clicked.connect(self.toggle_max_restore)

        #윈도우 프레임 이동
        self.dragger = WindowDragger(self.ui.framebar, self)

        self.ui.viewClipButton.clicked.connect(self.open_clip_list)

        self.ui.clipList.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.ui.scrollAreaWidgetContents.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # clipList의 부모 위젯(예: rightPanel)이 있다면 Expanding으로
        if hasattr(self.ui, "rightPanel"):
            self.ui.rightPanel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # clipList가 들어있는 레이아웃이 있다면 stretch도 강제 적용
        if hasattr(self.ui, "rightLayout"):
            self.ui.rightLayout.setStretchFactor(self.ui.clipList, 1)

        self.ui.optionButton.clicked.connect(self.open_option)

        #스페이스바는 keyPressEvent에서만 동작하도록 QPushButton이 포커스 없앰. 
        #재생 상태에 따라 아이콘 변경되게 했더니 스페이스바로 조작시 두번 실행되는 오류 수정
        self.ui.playVideoButton.setFocusPolicy(Qt.NoFocus) 
        
    def on_load_video(self, on):
        if on:
            self.populate_main_clip_list(self.timeline_data)

    def populate_main_clip_list(self, timeline_data):
        layout = self.ui.verticalLayout_2
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        self.clip_widgets = []
        for clip in timeline_data:
            # start_time을 초로 변환
            start_sec = time_to_sec(clip["start_time"])
            # end_time은 option에서 받은 self.clipLength만큼 더해서 계산
            end_sec = start_sec + self.clipLength
            end_time = sec_to_time(min(self.video_hander.videoLength, end_sec))
            key = (clip["start_time"], end_time)
            clip_widget = ClipWidget(
                self.video_hander.path,
                self.video_hander.fps,
                start_time=clip["start_time"],
                end_time=end_time,
                description=clip.get("description", ""),
                show_description=True  # 설명 표시
            )
            # 체크박스 상태 동기화
            clip_widget.checkbox.setChecked(self.clip_check_state.get(key, False))
            clip_widget.checkbox.stateChanged.connect(lambda state, k=key: self.on_clip_checkbox_changed(k, state))
            # 타임라인 클릭 시 영상 이동 연결
            clip_widget.time_selected.connect(self.seek_video_to_time)
            self.clip_widgets.append(clip_widget)
            layout.addWidget(clip_widget)

            layout.addStretch()
            self.resize_clip_widgets()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.resize_clip_widgets()

    def resize_clip_widgets(self):
        width = self.ui.clipList.viewport().width() - 20  # 여백 감안
        for w in getattr(self, 'clip_widgets', []):
            w.setMinimumWidth(width)
            w.setMaximumWidth(width)

    def open_clip_list(self):
        # viewall 창이 이미 열려있다면 또 생성하지 않게
        if hasattr(self, 'viewall_window') and self.viewall_window.isVisible():
            self.viewall_window.raise_()
            self.viewall_window.activateWindow()
            return
        # viewall 창을 열 때, 체크 상태를 넘겨줌
        self.viewall_window = UiForm(
            timeline_data = self.timeline_data,
            check_state = self.clip_check_state,
            player = self.video_hander.player,
            clipLength = self.clipLength,
            path = self.video_hander.path,
            fps = self.video_hander.fps,
            videoLength= self.video_hander.videoLength
        )
        self.viewall_window.checkbox_changed.connect(self.on_clip_checkbox_changed_from_viewall)
        self.viewall_window.makeclip.connect(self.on_makeclip)
        self.viewall_window.show() # exec() 대신 show() 사용 //viewall 창이 열려있어도 main창 조작 가능

    def on_makeclip(self, push, out_path):
        if push:
            ClipMaker(
                self.video_hander.path,
                self.startPoint,
                self.clipLength,
                self.clip_check_state,
                out_path
                )

    def open_option(self):
        if hasattr(self, 'option_window') and self.option_window.isVisible():
            return
        
        self.option_window = UiOption(self.video_hander.get_path(), self.startPoint, self.clipLength, self.skipFrame)
        self.option_window.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.option_window.optionApplied.connect(self.apply_option_values)
        
        self.option_window.show()

    def apply_option_values(self, path, startPoint, clipLength, skipFrame):
        # 받은 값을 적용
        self.path = path
        self.startPoint = startPoint
        self.clipLength = clipLength
        self.skipFrame = skipFrame
    
        # 옵션 적용 시 클립 리스트 갱신
        self.populate_main_clip_list(self.timeline_data)
        self.option_window.changePath.connect(self.on_change_path)

    def on_change_path(self, isChanged):
        if isChanged:
            if self.video_hander.player.is_playing():
                self.video_hander.player.stop()

                QTimer.singleShot(500, self._apply_new_path)  # 약 100ms 권장
            else:
                self._apply_new_path()

    def _apply_new_path(self):
        self.video_hander.set_option(self.path, self.skipFrame)
        self.video_hander.play_from_path()

    def on_clip_checkbox_changed(self, key, state):
        # 메인에서 체크박스 변경 시 상태 저장 및 viewall에도 반영
        self.clip_check_state[key[0]] = bool(state)
        if hasattr(self, 'viewall_window'):
            self.viewall_window.update_checkbox_state(key, bool(state))

    def on_clip_checkbox_changed_from_viewall(self, key, state):
        # viewall에서 체크박스 변경 시 메인에도 반영
        self.clip_check_state[key[0]] = bool(state)
        for w in getattr(self, 'clip_widgets', []):
            if (w.start_time, w.end_time) == key:
                w.checkbox.setChecked(bool(state))

    def toggle_max_restore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def on_video_click(self, event):
        if event.button() == Qt.LeftButton:
            self.video_hander.load_play()

    def seek_video_to_time(self, time_str):
        # "hh:mm:ss" → ms 변환
        h, m, s = map(int, time_str.split(":"))
        ms = (h * 3600 + m * 60 + s) * 1000
        self.video_hander.player.set_time(ms)


# 영상 출력부
class VideoPlayerHandler(QObject):
    load_video = Signal(bool)

    def __init__(self, parent: QWidget, ui, path, skipFrame):
        super().__init__(parent)
        self.parent = parent
        self.ui = ui
        self.video_widget = ui.videoPlayer
        self.slider = ui.playSlider
        self.fps = 30
        self.path = path
        self.skipFrame = skipFrame
        self.videoLength = 0

        # 영상 출력부
        self.vlc_instance = vlc.Instance("--no-plugins-cache")
        self.player = self.vlc_instance.media_player_new()

        # 재생 슬라이더
        self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.update_slider)

        self.slider.setMaximum(1000)
        self.slider.sliderMoved.connect(self.slider_moved)

        # 영상 버튼
        ui.playVideoButton.clicked.connect(self.toggle_play_pause)
        ui.skipForwardButton.clicked.connect(self.next_frame)
        ui.skipBackwardButton.clicked.connect(self.prev_frame)
        ui.playSpeedDoubleSpinBox.valueChanged.connect(self.set_playback_speed)

        # 영상 소리 조작
        #ui.toggleMuteButton.clicked.connect(self.toggle_mute)
        ui.toggleMuteButton.clicked.connect(self.start_ai)
        ui.volumeSpinBox.valueChanged.connect(self.set_volume)
        ui.volumeBar.valueChanged.connect(ui.volumeSpinBox.setValue)


    def start_ai(self):
        llm_output = assemble.start(self.path)
        self.timeline_data = utils.dic_to_ui_dic(llm_output)
        
    # 소리 뮤트
    def toggle_mute(self):
        is_muted = self.player.audio_get_mute()

        if not is_muted:
            self.last_volume = self.player.audio_get_volume()
            self.player.audio_set_mute(True)
            self.ui.volumeSpinBox.setValue(0)
        else:
            self.player.audio_set_mute(False)
            self.player.audio_set_volume(self.last_volume)
            self.ui.volumeSpinBox.setValue(self.last_volume)

    # 소리조절
    def set_volume(self, volume):
        self.player.audio_set_volume(volume)

    # 다음 프레임으로 이동
    def next_frame(self):
        if self.player.is_playing():
            self.player.pause()
            for _ in range(3):
                self.player.next_frame()
            self.player.play()
        else:
            for _ in range(3):
                self.player.next_frame()
            QTimer.singleShot(10, self.update_slider)

    # 이전 프레임으로 이동
    def prev_frame(self):
        if self.player.is_playing():
            self.player.pause()
            current_time = self.player.get_time()
            # ms_per_frame = 1 프레임
            ms_per_frame = int(1000 / self.fps)
            new_time = max(0, current_time - ms_per_frame*self.skipFrame)
            self.player.set_time(new_time)
            self.player.play()
        else:
            current_time = self.player.get_time()
            ms_per_frame = int(1000 / self.fps)
            new_time = max(0, current_time - ms_per_frame*self.skipFrame)
            self.player.set_time(new_time)
            QTimer.singleShot(10, self.update_slider)

    # DoubleSpinbox에서 수치를 읽어 영상 재생 속도에 적용
    def set_playback_speed(self):
        rate = self.ui.playSpeedDoubleSpinBox.value()
        self.player.set_rate(rate)        

    # 영상 주소 읽기 + 영상 플레이
    def load_play(self):
        self.path, _ = QFileDialog.getOpenFileName(
            self.parent, "영상 파일 선택", "", "Video Files (*.mp4 *.avi *.mkv)"
        )
        
        self.play_from_path()

    def play_from_path(self):
        if self.path:
            media = self.vlc_instance.media_new(self.path)
            self.fps = self.get_video_fps(self.path)
            self.player.set_media(media)
            self.update_video_length(media)
            try:
                self.player.set_hwnd(int(self.video_widget.winId()))
            except Exception as e:
                print(f"Failed to set video widget: {e}")
                
            self.emit_load_video()
            self.timer.start()
            self.player.play()
            QTimer.singleShot(200, self.player.pause)
        else:
            return

    # 영상 위치에 따라 슬라이더 값 조절
    def update_slider(self):
        if self.player.is_playing():
            length = self.player.get_length()
            current_time = self.player.get_time()
            if length > 0:
                current_time = self.player.get_time()
                pos = int(current_time * 1000 / length)
                self.slider.blockSignals(True)
                self.slider.setValue(pos)
                self.slider.blockSignals(False)

                # 영상 시간 출력 "00:00:00 / 00:00:00"
                self.ui.videoTime.setText(f"{self.ms_to_hms(current_time)} / {self.ms_to_hms(length)}")      

    # 사용자가 슬라이더를 움직여 영상 재생 위치 변화
    def slider_moved(self, position):
        length = self.player.get_length()
        if length > 0:
            new_time = int(length * position / 1000)
            self.player.set_time(new_time)

    # 재생 정지 토글 버튼
    def toggle_play_pause(self):
        if self.player.is_playing():
            self.player.pause()
            self.ui.playVideoButton.setIcon(self.ui.icon_play)
        else:
            self.player.play()
            self.ui.playVideoButton.setIcon(self.ui.icon_pause)

    # 밀리초 -> 시분초 형태
    @staticmethod
    def ms_to_hms(ms):
        seconds = ms // 1000
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02d}:{m:02d}:{s:02d}"

    # 영상 FPS 정보 가져오기
    def get_video_fps(self, path):
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            return None
        fps = cap.get(cv2.CAP_PROP_FPS)
        cap.release()
        return fps
    
    def set_option(self, path, skipFrame):
        self.path = path
        self.skipFrame = skipFrame

    def get_path(self):
        return self.path

    def emit_load_video(self):
        self.load_video.emit(True)

    def update_video_length(self, media):
        media.parse()
        self.videoLength = media.get_duration() / 1000


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

def start():
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
