import cv2
import matplotlib.pyplot as plt
import numpy as np



def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),50,(255,0,0),-1)

    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),50,(0,255,0),-1)


drawing=False
ix,iy=-1,-1
def draw_rectangle(event,x,y,flgas,param):
    global ix,iy,drawing
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)


cv2.namedWindow('Blank')
#cv2.setMouseCallback('Blank',draw_circle)
cv2.setMouseCallback('Blank',draw_rectangle)

img=np.zeros((512,512,3),np.uint8)

while True:
    cv2.imshow('Blank',img)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()







