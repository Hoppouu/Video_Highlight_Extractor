
import whisper
import datetime
import os
import librosa
import soundfile as sf
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import pandas as pd

yamnet_model = hub.load('https://tfhub.dev/google/yamnet/1')
class_map_path = tf.keras.utils.get_file(
    'yamnet_class_map.csv',
    'https://raw.githubusercontent.com/tensorflow/models/master/research/audioset/yamnet/yamnet_class_map.csv')
class_map_df = pd.read_csv(class_map_path)
yamnet_classes = class_map_df['display_name'].tolist()

def format_srt_timestamp(seconds: float) -> str:
    td = datetime.timedelta(seconds=seconds)
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    milliseconds = int(td.microseconds / 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def detect_laughter_scream(wav, sr, threshold=0.2):
    if sr != 16000:
        wav = librosa.resample(wav, orig_sr=sr, target_sr=16000)
        sr = 16000
    scores, _, _ = yamnet_model(wav)
    mean_scores = tf.reduce_mean(scores, axis=0).numpy()

    labels = []
    if mean_scores[yamnet_classes.index("Laughter")] > threshold:
        labels.append("[웃음]")
    if mean_scores[yamnet_classes.index("Screaming")] > threshold:
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

    parser = argparse.ArgumentParser(description="Whisper + YAMNet으로 라벨 포함 SRT 자막 생성기")
    parser.add_argument("audio_file", help="오디오 파일 경로 (MP3/WAV 등)")
    parser.add_argument("--model", default="base", help="Whisper 모델 크기 (tiny, base, small, medium, large)")
    parser.add_argument("--threshold", type=float, default=0.2, help="YAMNet 감지 신뢰도 기준 (0~1 사이)")
    args = parser.parse_args()

    transcribe_to_srt_with_labels(args.audio_file, model_size=args.model, threshold=args.threshold)
