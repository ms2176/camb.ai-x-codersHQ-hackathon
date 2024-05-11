import streamlit as st
import numpy as np
from run import run_video
import time
from sending_email import send_email
from uploading import uploading_file
from dub import dubbing
import os
import shutil
import webbrowser


run_video()
print("Recording Completed")
link = uploading_file('MyAVRecording.mp4')
print(link)
print("file uploaded")
u_link = dubbing(link, 125)
print("Video has been dubbed successfully!")
print(u_link)
# Move the file from the Downloads folder to the current folder


webbrowser.open(u_link)


downloads_folder = os.path.expanduser("~\Downloads")
current_folder = os.getcwd()
file_name = "output_video.mkv"
source_path = os.path.join(downloads_folder, file_name)
destination_path = os.path.join(current_folder, file_name)
shutil.move(source_path, destination_path)
user_link = uploading_file('output_video.mp4')
print(user_link)
send_email(user_link)









