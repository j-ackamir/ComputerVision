import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

nadia=cv2.imread('DATA/Nadia_Murad.jpg',0)
denis=cv2.imread('DATA/Denis_Mukwege.jpg',0)
solvay=cv2.imread('DATA/solvay_conference.jpg',0)

face_cascade=cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('DATA/haarcascades/haarcascade_eye.xml')

def detect_face(img):
    face_img=img.copy() #Sending pointer of img so modify directly w/o .copy()
    face_rects=face_cascade.detectMultiScale(face_img,1.2,5) #img,scaleFactor,minNeighbors
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(0,255,0),10)

    return face_img

def detect_eye(img):
    eye_img=img.copy() #Sending pointer of img so modify directly w/o .copy()
    eye_rects=eye_cascade.detectMultiScale(eye_img,1.2,5) #img,scaleFactor,minNeighbors
    for (x,y,w,h) in eye_rects:
        cv2.rectangle(eye_img,(x,y),(x+w,y+h),(255,255,255),10)

    return eye_img

cap=cv2.VideoCapture(0)
# fps = cap.get(cv2.CAP_PROP_FPS)
# print("Frames per second:", fps)
while True:
    ret,frame=cap.read()
    frame=detect_face(frame)
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(700,700))
    # time.sleep(1/60)
    cv2.imshow('Face Detected',frame)
    if cv2.waitKey(1) & 0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()

# result=detect_face(denis)
# plt.imshow(result,cmap='gray')
# plt.show()
# result=detect_eye(nadia)
# plt.imshow(result,cmap='gray')
# plt.show()
