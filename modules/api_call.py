import os
import sys
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modules import text_divide
from modules import utils

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

def call(file_name):
    #자막파일 불러오기
    file_path = file_name 
    subtitles = utils.ead_srt_file(file_path)

    for subtitle in subtitles:
        print(subtitle)

    #배열의 값을 하나의 문자열로 만들기
    full_text = '\n\n'.join(
        f"{sub.start} --> {sub.end}\n{sub.text}"
        for sub in subtitles
    )
    
    system_input = """
    지금부터 주어지는 텍스트는 인터넷 방송에서 게임을 하는 유저의 말들이야.
    텍스트를 보고 영상의 하이라이트라고 생각되는 부분을 타임스탬프와 그 이유와함께 말해줘.
    주로 게임에서 전투가 발생하거나, 누가 위험하거나, 죽거나 하는 부분을 중심으로 골라줘.
    출력 양식은 [시간대] : [내용]으로 해줘. 이유는 설명하지마.
    """
    chunks = text_divide.split_text_into_chunks(file_path="sample.srt")
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

    for time, text in responses_dict.items():
        print(f"{time}: {text}")

    with open("final.txt", "w", encoding="utf-8") as f:
        for time, text in responses_dict.items():
            f.write(f"{time} : {text}\n")