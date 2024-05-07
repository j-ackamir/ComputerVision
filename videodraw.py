import numpy as np
import matplotlib.pyplot as plt
import cv2

cap=cv2.VideoCapture(0)
width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Top left corner
# x=width//2
# y=height//2

#Increment for x and y
# w=width//4
# h=height//4

pt1=(0,0)
pt2=(0,0)
tL_clicked=False
bR_clicked=False

def draw_rectangle(event,x,y,flags,param):
    global pt1,pt2,tL_clicked,bR_clicked

    if event==cv2.EVENT_LBUTTONDOWN:
        if tL_clicked==True and bR_clicked==True:
            pt1=(0,0)
            pt2=(0,0)
            tL_clicked=False
            bR_clicked=False

        if tL_clicked==False:
            pt1=(x,y)
            tL_clicked=True

        elif bR_clicked==False:
            pt2=(x,y)
            bR_clicked=True
    
    

cv2.namedWindow('frame')
cv2.setMouseCallback('frame',draw_rectangle)


while True:
    ret,frame=cap.read()
    #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),5)
    if tL_clicked:
        cv2.circle(frame,center=pt1,radius=5,color=(0,0,255),thickness=-1)

    if tL_clicked and bR_clicked:
        cv2.rectangle(frame,pt1,pt2,(0,0,255),3)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()