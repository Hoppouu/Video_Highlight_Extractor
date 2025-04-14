import yt_dlp
import os
import ffmpeg

ydl_opts = {
    'format': 'bestaudio/best',
    'extract_audio': True,             # 오디오만 추출
    'audio_format': 'mp3',             # mp3 형식으로 변환
    'outtmpl': '%(title)s.%(ext)s',    # 저장 파일 이름 형식 (제목.mp3)
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',   # FFmpeg을 사용해 오디오 추출
        'preferredcodec': 'mp3',
        'preferredquality': '192',     # 품질: 192kbps
    }],
}

# url을 입력받으면 mp3를 다운로드함.
def download_sound_with_ytdlp(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def set_directory(dir):
    global directory
    directory = dir
    
directory = "./"