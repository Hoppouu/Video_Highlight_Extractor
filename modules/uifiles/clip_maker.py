from datetime import datetime
import os
from PySide6.QtGui import QImage, QPixmap
import cv2
from moviepy import VideoFileClip
from modules.uifiles.utils import time_to_sec
from modules import constants

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
    def from_video(video_path, fps, start_time, index):
        save_base_path="thumbnail",  # 확장자 없이 기본 경로
        cap = cv2.VideoCapture(video_path)
        cap.set(cv2.CAP_PROP_POS_FRAMES, fps * time_to_sec(start_time))
        ret, frame = cap.read()
        cap.release()

        if not ret:
            print(f"[{index}] 썸네일 추출 실패")
            return

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w
        qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        save_path = f"{constants.file_path_images}/{index}.jpg"
        saved = qimg.save(save_path)
        
        # 저장 경로 생성
        if saved:
            print(f"[{index}] 썸네일 저장 완료: {save_path}")
        else:
            print(f"이미지 저장 실패: {save_path}")
