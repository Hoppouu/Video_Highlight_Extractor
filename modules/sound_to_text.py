import whisper
import datetime
import os

def format_srt_timestamp(seconds: float) -> str:
    td = datetime.timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    milliseconds = int(td.microseconds / 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def write_srt(segments, file):
    for i, segment in enumerate(segments, start=1):
        start = format_srt_timestamp(segment['start'])
        end = format_srt_timestamp(segment['end'])
        text = segment['text'].strip()

        file.write(f"{i}\n")
        file.write(f"{start} --> {end}\n")
        file.write(f"{text}\n\n")

def transcribe_to_srt(audio_path, model_size="base"):
    model = whisper.load_model(model_size)
    print("🧠 모델 로딩 완료. 변환 시작...")

    result = model.transcribe(audio_path, verbose=True)
    
    base_name = os.path.splitext(audio_path)[0]
    srt_path = base_name + ".srt"

    with open(srt_path, "w", encoding="utf-8") as srt_file:
        write_srt(result["segments"], file=srt_file)

    print(f"✅ SRT 자막 저장 완료: {srt_path}")

# 실행 예시
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Whisper로 SRT 자막 생성기")
    parser.add_argument("audio_file", help="자막을 추출할 오디오 파일 경로")
    parser.add_argument("--model", default="base", help="모델 크기 (tiny, base, small, medium, large)")
    args = parser.parse_args()

    transcribe_to_srt(args.audio_file, model_size=args.model)