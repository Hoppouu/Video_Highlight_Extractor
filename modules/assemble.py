import os
from modules import extractor_url, sound_to_text, api_call
from modules import constants

def get_file_name(file_path : str):
    base_name = os.path.basename(file_path)
    name_without_ext = os.path.splitext(base_name)[0]
    return name_without_ext

def make_filename(file_path : str, extention: str):
     new_filename = file_path + "." + extention
     return new_filename
 

def start(file_path: str):
    try:
        file_name = get_file_name(file_path)
        f1 = file_path
        f2 = constants.file_path_subtitle + make_filename(file_name, "srt")
        f3 = constants.file_path_llm_outputs + make_filename(file_name, "txt")
        sound_to_text.start(f1, f2, model='medium')
        api_call.call(f2, f3)

        return f3
    except Exception as e:
        print(f"오류 발생: {e}")
        return ""
    