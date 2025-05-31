from PySide6.QtCore import QEvent, QObject, Qt

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