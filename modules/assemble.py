from modules import extractor_url, sound_to_text, api_call

file_path_origin = "./result/"
file_path_subtitle = file_path_origin + "subtitles/"
file_path_llm_outputs = file_path_origin + "llm_outputs/"

def get_file_name(file_path : str):
    import os
    new_filename = os.path.splitext(file_path)[0]
    return new_filename

def file(file_path : str, extention: str):
     new_filename = + "." + extention
     return new_filename
 

def start(file_path: str):
    try:
        file_name = get_file_name(file_path)
        f1 = file_path
        f2 = file_path_subtitle + file(file_name, "srt")
        f3 = file_path_llm_outputs + file(file_name, "txt")
        sound_to_text.start(f1, f2, model='medium')
        api_call.call(f2, f3)

        return f3
    except Exception as e:
        print(f"오류 발생: {e}")
        return ""
    