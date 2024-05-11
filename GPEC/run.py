import time
from AVrecordeR import start_AVrecording, stop_AVrecording, file_manager
import moviepy.editor as moviepy
def run_video():
    start_AVrecording("MyAVRecording")
    time.sleep(10)
    stop_AVrecording("MyAVRecording")
    file_manager("MyAVRecording")
    print("converting")
    clip = moviepy.VideoFileClip("MyAVRecording.avi")
    clip.write_videofile("MyAVRecording.mp4")
    print("converted")


