from openai import OpenAI
import text_divide

client = OpenAI(
  api_key="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"
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


class Subtitle:
    def __init__(self, index, start, end, text):
        self.index = index
        self.start = start
        self.end = end
        self.text = text.strip()
    
    def __str__(self):
        return f"{self.index}\n{self.start} --> {self.end}\n{self.text}\n"

def read_srt_file(file_path, fraction = 1):
    subtitles = []
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()
    
    index = 1
    while index < len(lines):
        if lines[index].strip().isdigit():
            index += 1
            time_line = lines[index].strip()
            start, end = time_line.split(' --> ')
            index += 1
            text = ""
            while index < len(lines) and lines[index].strip() != "":
                text += lines[index]
                index += 1
            subtitle = Subtitle(len(subtitles) + 1, start, end, text)
            subtitles.append(subtitle)
        index += 1
    count = int(len(subtitles) * fraction)
    subtitles = subtitles[:count]
    return subtitles

def get_dict(full_text):
    subtitles = {}
    lines = full_text.strip().splitlines()

    for line in lines:
        line = line.strip()
        if line.startswith('[') and ']' in line:
            end_idx = line.index(']')
            timestamp_part = line[1:end_idx]
            if len(timestamp_part) >= 8 and timestamp_part.count(':') == 2:
                time_key = timestamp_part.split(',')[0]
                rest = line[end_idx+1:].strip()
                if rest.startswith(':'):
                    rest = rest[1:].strip()
                sentence = rest.strip('"')
                subtitles[time_key] = sentence
    return subtitles

def call(file_name):
    #자막파일 불러오기
    file_path = file_name 
    subtitles = read_srt_file(file_path)

    for subtitle in subtitles:
        print(subtitle)

    #배열의 값을 하나의 문자열로 만들기
    full_text = '\n\n'.join(
        f"{sub.start} --> {sub.end}\n{sub.text}"
        for sub in subtitles
    )
    # print(full_text)
    system_input = """
    지금부터 주어지는 텍스트는 인터넷 방송에서 게임을 하는 유저의 말들이야.
    텍스트를 보고 영상의 하이라이트라고 생각되는 부분을 타임스탬프와 그 이유와함께 말해줘.
    주로 게임에서 전투가 발생하거나, 누가 위험하거나, 죽거나 하는 부분을 중심으로 골라줘.
    출력 양식은 [시간대] : [내용]으로 해줘.
    [내용] 부분에는 자막의 내용만 넣어줘.
    """
    user_input = full_text
    responses = create_chat_completion(system_input, user_input)
    responses = responses.choices[0].message.content
    responses_dict = {}
    responses_dict.update(get_dict(responses))
    # 출력
    for time, text in responses_dict.items():
        print(f"{time}: {text}")

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
    responses_dict.update(get_dict(responses))


from collections import OrderedDict
responses_dict = OrderedDict(
    sorted(responses_dict.items(), key=lambda x: x[0])  # x[0]이 time (HH:MM:SS)
)

for time, text in responses_dict.items():
    print(f"{time}: {text}")

with open("final.txt", "w", encoding="utf-8") as f:
    for time, text in responses_dict.items():
        f.write(f"{time} : {text}\n")