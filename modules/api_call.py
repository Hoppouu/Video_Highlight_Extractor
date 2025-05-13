from openai import OpenAI

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

def read_srt_file(file_path, fraction = 0.2):
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

#자막파일 불러오기
file_path = 'sample.srt' 
subtitles = read_srt_file(file_path)

for subtitle in subtitles:
    print(subtitle)

#배열의 값을 하나의 문자열로 만들기
full_text = '\n\n'.join(
    f"{sub.start} --> {sub.end}\n{sub.text}"
    for sub in subtitles
)

print(full_text)



system_input = """
    너는 영상 하이라이트 추출기야. 영상은 인터넷 방송이야. 자막 내용을 주면 자막 내용을 보고 영상의 하이라이트라고 생각되는 부분을 타임스탬프와 그 이유와함께 말해줘.
    출력 양식은 [시간대] : [내용]으로 해줘.
"""
user_input = full_text
responses = create_chat_completion(system_input, user_input)
print(responses.choices[0].message.content)