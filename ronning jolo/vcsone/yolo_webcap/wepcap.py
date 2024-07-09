from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture(0)
cap.set(3,1480)
cap.set(4, 720)

model = YOLO("../YOLO/yolov8n.pt")

while True:
    success, img = cap.read()
    resuts = model(img, stream= True)
    for r in resuts:
        boxes = r.boxes
        for box in boxes:
            x1,y1,x2,y2 = box.xyxy[0]
           
           # bbox = int(x1),int(y1),int(w),int(h)
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
           # print(x1,y1,x2,y2)
           
           # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
           # x1,y1,w,h = box.xywh[0]
           
            w,h = x2-x1,y2-y1
           # bbox = int(x1), int(y1), int(w), int(h)
            cvzone.cornerRect(img,(x1,y1,w,h))
            conf = math.ceil((box.conf[0]*100))/100
            print(conf)
            cvzone.putTextRect(img,f'{conf}',(max(0,x1),max(0,y2-20)))
            
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    
