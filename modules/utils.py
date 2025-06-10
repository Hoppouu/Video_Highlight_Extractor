def dic_to_ui_dic(file_path: str) -> list:
    timeline_data = []
    if(file_path == ""):
        return
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            if ' : ' in line:
                parts = line.strip().split(' : ', 1)
                if len(parts) == 2:
                    start_time, description = parts
                    timeline_data.append({
                        "start_time": start_time.strip(),
                        "description": description.strip()
                    })
    return timeline_data

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
        if len(line) < 12: #너무 짧으면 건너 뛰기
            continue

        time_part = line[:12]
        if time_part.count(':') == 2 and ',' in time_part:
            time_key = time_part.split(',')[0]
            rest = line[13:].strip()

            parts = rest.split(':')
            if len(parts) >= 2:
                content = f"{parts[0].strip()} : {parts[1].strip()}"
            else:
                content = rest

            subtitles[time_key] = content.strip('"')
    return subtitles

