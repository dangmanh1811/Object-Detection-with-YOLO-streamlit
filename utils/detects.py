import numpy as np
import cv2
import streamlit as st
import tempfile
from config.CONFIG import *
import time

# Object Detection on an image
def detect_objects_on_image(image):
    img_array = np.array(image)
    results = model(img_array)
    annotated_image = results[0].plot()
    return annotated_image

# Object Detection on a video
def detect_objects_on_video(video_file):
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(video_file.read())
    cap = cv2.VideoCapture(tfile.name)
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        annotated_frame = results[0].plot()
        stframe.image(annotated_frame, channels="BGR", use_column_width=True)

    cap.release()
    
# Object detection real-time from webcam
def detect_objects_real_time():
    cap = cv2.VideoCapture(0)
    stframe = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        annotated_frame = results[0].plot() 
        stframe.image(annotated_frame, channels="BGR", use_column_width=True)
        time.sleep(0.03)

    cap.release()