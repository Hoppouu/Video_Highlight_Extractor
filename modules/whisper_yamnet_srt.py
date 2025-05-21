import whisper
import datetime
import os
import librosa
import torch
import numpy as np
import pandas as pd
from panns_inference import AudioTagging

# PANNs Cnn14 모델 불러오기 (torch hub)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
panns_model = AudioTagging(checkpoint_path=None)
panns_model.to(device)
panns_model.eval()

# PANNs AudioSet 클래스 이름 (출처: https://github.com/qiuqiangkong/audioset_tagging_cnn)
# 중요한 'Laughter'와 'Screaming' 포함됨
panns_class_map = [
    "Speech", "Music", "Laughter", "Screaming",
    # ... 필요시 전체 527개 클래스 넣을 수 있음
]

def format_srt_timestamp(seconds: float) -> str:
    td = datetime.timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    milliseconds = int(td.microseconds / 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def detect_laughter_scream(wav, sr, threshold=0.2):
    # PANNs는 32000Hz 입력
    if sr != 32000:
        wav = librosa.resample(wav, orig_sr=sr, target_sr=32000)
        sr = 32000
    
    # 모델 입력용 변환
    wav = torch.tensor(wav, dtype=torch.float32).to(device)
    if wav.dim() == 1:
        wav = wav.unsqueeze(0)  # (1, samples)
    
    with torch.no_grad():
        output_dict = panns_model(wav)
    scores = output_dict['clipwise_output'].cpu().numpy()[0]  # (527,)

    labels = []
    # 'Laughter'는 클래스 인덱스 2, 'Screaming'은 3 (위 배열 기준)
    if scores[2] > threshold:
        labels.append("[웃음]")
    if scores[3] > threshold:
        labels.append("[비명]")
    return " ".join(labels)

def write_srt(segments, audio_path, file, threshold=0.2):
    y, sr = librosa.load(audio_path, sr=None)

    for i, segment in enumerate(segments, start=1):
        start_sample = int(segment['start'] * sr)
        end_sample = int(segment['end'] * sr)
        clip = y[start_sample:end_sample]

        tags = detect_laughter_scream(clip, sr, threshold=threshold)
        text = segment['text'].strip() + (" " + tags if tags else "")

        start = format_srt_timestamp(segment['start'])
        end = format_srt_timestamp(segment['end'])

        file.write(f"{i}\n")
        file.write(f"{start} --> {end}\n")
        file.write(f"{text}\n\n")

def transcribe_to_srt_with_labels(audio_path, model_size="base", threshold=0.2):
    model = whisper.load_model(model_size)
    print("🎤 Whisper 모델 로딩 완료.")

    result = model.transcribe(audio_path, verbose=True)

    base_name = os.path.splitext(audio_path)[0]
    srt_path = base_name + "_tagged.srt"

    with open(srt_path, "w", encoding="utf-8") as srt_file:
        write_srt(result["segments"], audio_path, srt_file, threshold=threshold)

    print(f"✅ 라벨 추가된 SRT 저장 완료: {srt_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Whisper + PANNs(Cnn14)으로 라벨 포함 SRT 자막 생성기")
    parser.add_argument("audio_file", help="오디오 파일 경로 (MP3/WAV 등)")
    parser.add_argument("--model", default="base", help="Whisper 모델 크기 (tiny, base, small, medium, large)")
    parser.add_argument("--threshold", type=float, default=0.2, help="PANNs 감지 신뢰도 기준 (0~1 사이)")
    args = parser.parse_args()

    transcribe_to_srt_with_labels(args.audio_file, model_size=args.model, threshold=args.threshold)