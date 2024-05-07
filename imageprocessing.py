import cv2
import numpy as np
import matplotlib.pyplot as plt


def show_pic(img):
    fig=plt.figure(figsize=(15,15))
    ax=fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()



#img=cv2.imread('DATA/rainbow.jpg',0)
img=cv2.imread('DATA/crossword.jpg',0)
threshval,thresh1=cv2.threshold(img,180,255,cv2.THRESH_BINARY)
#threshval,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
##MULTIPLE DIFFERENT THRESHOLDING OPTIONS
plt.imshow(thresh1,cmap='gray')
plt.show()

#show_pic(thresh1)

th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
show_pic(th2)