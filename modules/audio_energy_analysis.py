#!/usr/bin/env python
# coding: utf-8

# 고에너지 구간 분석 (librosa 기반 - MP3 지원)
# 이 스크립트는 오디오 파일(MP3, WAV 등)의 에너지 변화를 분석하고
# 고에너지 구간을 출력 및 시각화합니다.

# 필요한 패키지 설치
# pip install librosa matplotlib numpy

import librosa
import numpy as np
import matplotlib.pyplot as plt

# 오디오 로딩 (MP3, WAV 모두 지원)
file_path = "sample_audio.mp3"  # 또는 "sample_audio.wav"
signal, sample_rate = librosa.load(file_path, sr=None)

# Short-term feature 추출
win_size = 0.05     # 50ms
step_size = 0.025   # 25ms
win_samples = int(win_size * sample_rate)
step_samples = int(step_size * sample_rate)

# Framing
frames = librosa.util.frame(signal, frame_length=win_samples, hop_length=step_samples).T

# 에너지 계산 (프레임별 제곱합)
energy = np.sum(frames ** 2, axis=1)
times = np.arange(0, len(energy)) * step_size

# 상위 10% 이상 에너지 시간 출력
energy_threshold = np.percentile(energy, 90)
high_energy_times = times[energy > energy_threshold]
print("고에너지 구간 (상위 10%):")
for t in high_energy_times:
    print(f"{t:.2f}초")

# 에너지 시각화
plt.figure(figsize=(10, 4))
plt.plot(times, energy, label="Short-term Energy")
plt.axhline(energy_threshold, color='r', linestyle='--', label=f"Threshold ({energy_threshold:.3f})")
plt.title("Energy over Time")
plt.xlabel("Time (s)")
plt.ylabel("Energy")
plt.legend()
plt.tight_layout()
plt.show()
