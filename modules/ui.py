import sys
from PySide6.QtWidgets import QFileDialog, QMainWindow, QApplication
from PySide6.QtCore import QUrl, Qt
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from uifiles.ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowFlag(Qt.FramelessWindowHint)
        
        #프레임 조작
        self.ui.closeWindow.clicked.connect(QApplication.quit)
        self.ui.minimizeWindow.clicked.connect(self.showMinimized)
        self.ui.toggleMaximizeRestore.clicked.connect(self.toggle_max_restore)

        #영상 출력부
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.ui.videoPlayer)
        
        
        self.ui.videoPlayer.mousePressEvent = self.open_video_file

        # 슬라이더 이벤트 연결 (추가)
        self.ui.playSlider.sliderMoved.connect(self.set_position)
        self.media_player.positionChanged.connect(self.update_slider)
        self.media_player.durationChanged.connect(self.set_duration)

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
                self.media_player.setSource(QUrl.fromLocalFile(file_path))
                self.media_player.play()

                # (추가) 클릭 이벤트 제거 – 더 이상 영상 열기 안 됨
                self.ui.videoPlayer.mousePressEvent = lambda event: None

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
