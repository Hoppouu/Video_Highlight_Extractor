import os
import subprocess
import time
import sys
from PySide6.QtWidgets import QDialog, QFileDialog, QMainWindow, QApplication, QWidget, QMessageBox
from PySide6.QtCore import QUrl, Qt, QObject, QEvent, QTimer, Signal, QThread
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from uifiles.ui_main import Ui_MainWindow
from uifiles.ui_Clip_list import Ui_Form

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #윈도우 프레임 제거
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        #프레임 조작
        self.ui.closeWindow.clicked.connect(QApplication.quit)
        self.ui.minimizeWindow.clicked.connect(self.showMinimized)
        self.ui.toggleMaximizeRestore.clicked.connect(self.toggle_max_restore)

        #프레임 이동
        self.dragger = WindowDragger(self.ui.framebar, self)

        #영상 출력부
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.ui.videoPlayer)
        
        
        self.ui.videoPlayer.mousePressEvent = self.open_video_file

        # 슬라이더 이벤트 연결
        self.ui.playSlider.sliderMoved.connect(self.set_position)
        self.media_player.positionChanged.connect(self.update_slider)
        self.media_player.durationChanged.connect(self.set_duration)

        self.ui.viewClipButton.clicked.connect(self.open_clip_list)

    def open_clip_list(self):
        self.ui.viewClipButton = UiForm()
        self.ui.viewClipButton.exec()

    def set_position(self, position):
         self.media_player.setPosition(position)

    def update_slider(self, position):
            self.ui.playSlider.setValue(position)

    def set_duration(self, duration):
        self.ui.playSlider.setRange(0, duration)

    def toggle_max_restore(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def open_video_file(self, event):
        if event.button() == Qt.LeftButton:
            file_path, _ = QFileDialog.getOpenFileName(self, "영상 파일 선택", "", "Video Files (*.mp4 *.avi *.mkv)")
        
            if file_path:
                self.ffmpeg_thread = FFmpegThread(file_path)
                self.ffmpeg_thread.finished.connect(self.on_conversion_finished)
                self.ffmpeg_thread.error.connect(self.on_conversion_error)
                self.ffmpeg_thread.start()
                self.show_message("영상 변환 중...", "잠시만 기다려 주세요.", QMessageBox.Information)

    # 변환 완료 호출
    def on_conversion_finished(self, output_path):
        self.show_message("변환 완료", f"변환된 파일 경로: {output_path}", QMessageBox.Information)
        self.media_player.setSource(QUrl.fromLocalFile(output_path))
        self.media_player.play()

    # 변환 오류 호출
    def on_conversion_error(self, error_message):
        self.show_message("변환 오류", f"변환 중 오류가 발생했습니다: {error_message}", QMessageBox.Critical)

    # 메시지 박스
    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec()

    
#코덱 변환
class FFmpegThread(QThread):
    finished = Signal(str)  # 변환 완료 신호
    error = Signal(str)  # 오류 발생 신호

    def __init__(self, input_path, parent=None):
        super().__init__(parent)
        self.input_path = input_path
        self.elapsed_time = None

    def run(self):
        # ffmpeg 경로 설정
        ffmpeg_path = os.path.join(os.getcwd(), 'modules', 'ffmpeg', 'ffmpeg-7.1.1-essentials_build', 'bin', 'ffmpeg.exe')

        # 변환된 파일 경로 설정
        output_path = os.path.splitext(self.input_path)[0] + "_converted.mp4"
        
        # ffmpeg 명령어
        cmd = [
            ffmpeg_path,
            "-hwaccel", "cuda",       # GPU 디코딩
            "-i", self.input_path,
            # "-c:v", "libx264",   # CPU 인코딩
            "-c:v", "h264_nvenc",   # GPU 인코딩
            "-preset", "p4",
            "-c:a", "copy",
            "-y",
            output_path
        ]
        
        try:
            start_time = time.time()

            subprocess.run(cmd, check=True)  # 변환 실행

            end_time = time.time()
            
            print(f"{end_time - start_time:.3f}")

            self.finished.emit(output_path)  # 변환이 완료되면 신호를 보냄
        except subprocess.CalledProcessError as e:
            self.error.emit(str(e))  # 오류 발생 시 오류 메시지를 보냄

   

# 클립 리스트             
class UiForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        #윈도우 프레임 제거
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        #프레임 설정
        self.ui.closeWindowButton.clicked.connect(self.close)
        self.dragger = WindowDragger(self.ui.framebar, self)
        
     
# 윈도우 이동
class WindowDragger(QObject):
    def __init__(self, frame, window):
        super().__init__(frame)
        self.frame = frame  
        self.window = window
        self._start_pos = None

        self.frame.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.frame and not self.window.isMaximized():
            if event.type() == QEvent.MouseButtonPress and event.button() == Qt.LeftButton:
                self._start_pos = event.globalPosition().toPoint() - self.window.frameGeometry().topLeft()
                return True

            elif event.type() == QEvent.MouseMove and event.buttons() & Qt.LeftButton:
                if self._start_pos is not None:
                    self.window.move(event.globalPosition().toPoint() - self._start_pos)
                    return True

            elif event.type() == QEvent.MouseButtonRelease:
                self._start_pos = None
                return True

        return super().eventFilter(obj, event)



if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
