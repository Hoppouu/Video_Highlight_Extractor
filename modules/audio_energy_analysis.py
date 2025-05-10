import librosa
import numpy as np
import matplotlib.pyplot as plt

import os
print(os.getcwd())

# 오디오 로딩 (MP3, WAV 모두 지원)
# file_path = "./audio.mp3"  # 또는 "sample_audio.wav"

file_path = os.path.join(os.path.dirname(__file__), "audio.mp3")
signal, sample_rate = librosa.load(file_path, sr=None)


# Short-term feature 추출
win_size = 0.5     # 500ms
step_size = 0.25   # 250ms
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
