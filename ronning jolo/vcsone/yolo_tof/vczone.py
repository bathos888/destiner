from ultralytics import YOLO
import cv2


model = YOLO('../LOYO/yolov8l.pt')
results = model("yoloph/c2.jpg", show=True)
cv2.waitKey(0)