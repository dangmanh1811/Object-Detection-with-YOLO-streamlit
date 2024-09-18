import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import tempfile
import time
import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


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

if __name__ == '__main__':
    st.title("Object Detection")
    st.logo('./data/image/logo9.5AI.jpg ')
    
    # Load model YOLOv8
    model = YOLO('./modelweight/yolov10s.pt')
    
    # Add background
    img_file = './data/background/background.jpg'
    img_base64 = get_base64(img_file)
    page_bg_img = f'''
    <style>
    .stApp {{
    background-image: url("data:image/jpg;base64,{img_base64}");
    background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # List of options
    option1 = "Object Detection on an image"
    option2 = "Object Detection on a video"
    option3 = "Object Detection Real-time"

    task = st.sidebar.selectbox("Select your Object Detection: ", (option1, option2, option3))

    if task == option1:
        st.header(option1)
        uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        
        if uploaded_image is not None:
            image = Image.open(uploaded_image)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            
            if st.button("Detect Objects"):
                with st.spinner("Detecting..."):
                    annotated_image = detect_objects_on_image(image)
                    st.image(annotated_image, caption="Detected Image", use_column_width=True)

    elif task == option2:
        st.header(option2)
        uploaded_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

        if uploaded_video is not None:
            st.video(uploaded_video)
            if st.button("Detect Objects in Video"):
                detect_objects_on_video(uploaded_video)

    elif task == option3:
        st.header(option3)
        if st.button("Start Real-Time Detection"):
            detect_objects_real_time()
