from datetime import datetime
import os
from PySide6.QtGui import QImage, QPixmap
import cv2
from moviepy import VideoFileClip

from modules.uifiles.utils import time_to_sec

class ClipMaker():
    def __init__(self, path, startPoint, clipLength, clip_check_state, out_path):
        super(ClipMaker, self).__init__()

        clip = VideoFileClip(path)

        for start, checked in clip_check_state.items():
            if checked:
                start_sec = max(0, time_to_sec(start) + startPoint)
                end_sec = min(start_sec + clipLength, clip.duration)

                subclip = clip.subclipped(start_sec, end_sec)

                base_name = os.path.splitext(os.path.basename(path))[0]
                output_filename = f"{base_name}_{start.replace(':', '_')}.mp4"
                output_path = os.path.join(out_path, output_filename)

                subclip.write_videofile(
                    output_path,
                    preset="ultrafast",
                    threads = max(1, os.cpu_count() - 1)
                    )

                print(output_filename)

        clip.close()


# class ThumbnailMaker:
#     @staticmethod
#     def from_video(video_path, fps, start_time):
#         cap = cv2.VideoCapture(video_path)
#         cap.set(cv2.CAP_PROP_POS_FRAMES, fps * time_to_sec(start_time))
#         ret, frame = cap.read()
#         cap.release()

#         if not ret:
#             return None

#         rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         h, w, ch = rgb.shape
#         bytes_per_line = ch * w
#         qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         return QPixmap.fromImage(qimg)

class ThumbnailMaker:
    @staticmethod
    def from_video(
        video_path,
        fps,
        start_time,
        crop_size=(360, 360),
        save_base_path="thumbnail",  # 확장자 없이 기본 경로
        index=0                      # 숫자 인덱스 추가
    ):
        cap = cv2.VideoCapture(video_path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, fps * time_to_sec(start_time))
        ret, frame = cap.read()
        cap.release()

        if not ret:
            print(f"[{index}] 썸네일 추출 실패")
            return

        # BGR → RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 중앙 crop
        h, w, _ = rgb.shape
        crop_w, crop_h = crop_size
        start_x = max((w - crop_w) // 2, 0)
        start_y = max((h - crop_h) // 2, 0)
        cropped = rgb[start_y:start_y+crop_h, start_x:start_x+crop_w]

        # 저장 경로 생성
        save_path = f"{save_base_path}_{index}.jpg"

        # 저장
        cv2.imwrite(save_path, cv2.cvtColor(cropped, cv2.COLOR_RGB2BGR))
        print(f"[{index}] 썸네일 저장 완료: {save_path}")