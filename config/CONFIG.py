from ultralytics import YOLO

model_path = "./modelweight/yolov10s.pt"
logo_path = "./data/image/logo9.5AI.jpg"
background_path = './data/background/background.jpg'
title = "Object Detection"
option1 = "Object Detection on an image"
option2 = "Object Detection on a video"
option3 = "Object Detection Real-time"

# Load model YOLOv8
model = YOLO(model_path)