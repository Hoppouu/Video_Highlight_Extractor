#Assemble files
from modules import extractor_url, sound_to_text, ui, api_call
from modules.uifiles.ui_main import Ui_MainWindow

def init_decorator(func):
    def wrapper(self, *args, **kwargs):
        print("초기화 전 작업")
        func(self, *args, **kwargs)
        print("초기화 후 작업")
    return wrapper

def set_MainWindow():
    ui.MainWindow.__init__ = init_decorator(ui.MainWindow.__init__)


def temp():
    str = input("URL을 입력해주세요 : ")  
    extractor_url.download_sound_with_ytdlp(str)
    sound_to_text.start("sample.webm", model='medium')
    api_call.call("sample.srt")
    
api_call.call("sample.srt")
#temp()
ui.start()
 