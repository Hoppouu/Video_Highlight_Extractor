#Assemble files
from modules import ui
from modules.uifiles.ui_main import Ui_MainWindow

def init_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("초기화 전 작업")
        func(self, *args, **kwargs)
        print("초기화 후 작업")
    return wrapper

def set_MainWindow():
    ui.MainWindow.__init__ = init_decorator(ui.MainWindow.__init__)

ui.start()
 