import os
import sys
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules import text_divide, utils

_ = load_dotenv(find_dotenv())
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

#쿼리를 생성해서 보내고 gpt의 응답을 반환한다.
def create_chat_completion(system_input, user_input, model="gpt-4o-mini", temperature=1.15, max_tokens=150):
    try:    
        messages = [
            {"role": "system", "content": system_input},
            {"role": "user", "content": user_input}
        ]                   
                                      
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
            # max_tokens=max_tokens
        )
        return response
    except Exception as e:
        return f"Error: {str(e)}"

from difflib import SequenceMatcher
from datetime import timedelta

def to_timedelta(t):
    h, m, s = map(int, t.split(":"))
    return timedelta(hours=h, minutes=m, seconds=s)

def is_similar(text1, text2, threshold=0.85):
    return SequenceMatcher(None, text1, text2).ratio() >= threshold

def deduplicate_highlights(responses_dict, min_gap_sec=10):
    items = sorted(responses_dict.items(), key=lambda x: to_timedelta(x[0]))
    result = []

    last_time = timedelta(seconds=-9999)
    last_text = ""

    for time_str, text in items:
        curr_time = to_timedelta(time_str)
        time_diff = (curr_time - last_time).total_seconds()

        if time_diff >= min_gap_sec and not is_similar(text, last_text):
            result.append((time_str, text))
            last_time = curr_time
            last_text = text

    return dict(result)


# def validate_highlights(responses_dict, subtitles, threshold=0.85):
#     validated = {}
#     subtitle_texts = [sub.text for sub in subtitles]

#     for time, text in responses_dict.items():
#         if any(is_similar(text, original, threshold) for original in subtitle_texts):
#             validated[time] = text
#     return validated

def validate_highlights_with_timestamps(responses_dict, subtitles, threshold=0.85):
    validated = {}

    for time, text in responses_dict.items():
        matched_time = None

        for sub in subtitles:
            if is_similar(text, sub.text, threshold):
                matched_time = sub.start
                break

        if matched_time:
            cleaned_time = matched_time.split(',')[0]
            validated[cleaned_time] = text

    return validated


def call(srt_path, llm_output):
    #자막파일 불러오기
    subtitles = utils.read_srt_file(srt_path)

    for subtitle in subtitles:
        print(subtitle)

    #배열의 값을 하나의 문자열로 만들기
    full_text = '\n\n'.join(
        f"{sub.start} --> {sub.end}\n{sub.text}"
        for sub in subtitles
    )
    
    system_input = """
    지금부터 주어지는 텍스트는 인터넷 방송에서 게임하는 유저들의 대화입니다.  
    텍스트를 분석해 영상에서 하이라이트라고 생각되는 장면을 타임스탬프와 함께 골라주세요.  
    하이라이트는 주로 전투 발생, 위험 상황, 죽음 등의 중요한 순간에 해당합니다.  
    각 하이라이트에 대해 왜 중요한지 단계별로 이유를 설명하며 판단해 주세요.  

    출력 형식은 아래와 같습니다.  
    출력에서는 절대 첫 줄에 "[시간대] : [내용] : [이유]" 같은 헤더 문구를 포함하지 말고, 각 줄은 아래 형식만 반복해서 출력해주세요. 

    [시간대] : [내용] : [이유]
    """
    
    chunks = text_divide.split_text_into_chunks(file_path=srt_path, max_chunk_size=25000, step=8000)
    # ten_percent_count = max(1, len(chunks) // 10)
    # chunks = chunks[:ten_percent_count]
    
    responses_dict = {}
    for i, chunk in enumerate(chunks):
        print(str(i + 1) + "/"+ str(len(chunks)))
        responses = create_chat_completion(system_input, chunk)
        responses = responses.choices[0].message.content
        print(responses)
        responses_dict.update(utils.get_dict(responses))

    from collections import OrderedDict
    responses_dict = OrderedDict(
        sorted(responses_dict.items(), key=lambda x: x[0])  # x[0]이 time (HH:MM:SS)
    )

    responses_dict = deduplicate_highlights(responses_dict)
    
    responses_dict = validate_highlights_with_timestamps(responses_dict, subtitles)
    
    responses_dict = OrderedDict(
        sorted(responses_dict.items(), key=lambda x: x[0])  # x[0]이 time (HH:MM:SS)
    )
    
    for time, text in responses_dict.items():
        print(f"{time}: {text}")
    
    with open(llm_output, "w", encoding="utf-8") as f:
        for time, text in responses_dict.items():
            f.write(f"{time} : {text}\n")