#Assemble files
import os
from modules import ui, constants
from modules.uifiles.ui_main import Ui_MainWindow

for path in constants.file_path:
    os.makedirs(path, exist_ok=True)

ui.start()
 