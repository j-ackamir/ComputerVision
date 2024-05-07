import numpy as np
import matplotlib.pyplot as plt
import cv2

def display_image(image, cmap='gray'):
    fig = plt.figure(figsize=(12,10))
    ax = fig.add_subplot(111)
    ax.imshow(image, cmap='gray')
    plt.show()

img=cv2.imread('DATA/pennies.jpg')

img=cv2.medianBlur(img,35)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

kernel=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2) 
display_image(opening)
sure_bg = cv2.dilate(opening,kernel,iterations=3)
display_image(sure_bg)
dist_transform=cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret,sure_fg=cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)

sure_fg=np.uint8(sure_fg)
unknown=cv2.subtract(sure_bg,sure_fg)

ret,markers=cv2.connectedComponents(sure_fg) #Associated each coin with a color
markers=markers+1 # bc unknown is 0 only
markers[unknown==255]=0
markers=cv2.watershed(img,markers)
image,contours,hierarchy=cv2.findContours(markers.copy(),cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    if hierarchy[0][i][3]==-1:
        cv2.drawContours(img,contours,i,(255,0,0),10)

#display_image(img)


