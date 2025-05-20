from openai import OpenAI
import re

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

def get_dict(full_text):
    subtitles = {}
    lines = full_text.strip().splitlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 타임스탬프 패턴 검사 : [HH:MM:SS,mmm] : ... 
        if line.startswith('[') and ']' in line:
            end_idx = line.index(']')
            timestamp_part = line[1:end_idx]  # '00:00:00,000'

            # 시간 형식 간단 체크: 8자리 이상이고 ':' 2개 있는지 확인
            if len(timestamp_part) >= 8 and timestamp_part.count(':') == 2:
                # 타임스탬프에서 ,000 부분 제외하고 시간만 가져오기
                time_key = timestamp_part.split(',')[0]  # '00:00:00'

                # 그 뒤에 있는 텍스트 뽑기 ("] : " 다음 부분)
                rest = line[end_idx+1:].strip()
                if rest.startswith(':'):
                    rest = rest[1:].strip()
                sentence = rest.strip('"')

                # 다음 줄을 설명으로 넣기 (있으면)
                explanation = ''
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if next_line != '':
                        explanation = next_line
                        i += 1  # 설명 줄은 다음 루프에서 건너뛰기 위해 +1

                # 딕셔너리에 저장
                if explanation:
                    subtitles[time_key] = f"{sentence} - {explanation}"
                else:
                    subtitles[time_key] = sentence
        i += 1
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
    너는 영상 하이라이트 추출기야. 영상은 인터넷 방송이야. 자막 내용을 주면 자막 내용을 보고 영상의 하이라이트라고 생각되는 부분을 타임스탬프와 그 이유와함께 말해줘.
    출력 양식은 [시간대] : [내용]으로 해줘.
    """
    user_input = full_text
    responses = create_chat_completion(system_input, user_input)
    responses = responses.choices[0].message.content
    responses_dict = get_dict(responses)
    # 출력
    for time, text in responses_dict.items():
        print(f"{time}: {text}")
