import numpy as np
import matplotlib.pyplot as plt
import cv2

def display_image(img):
    fig=plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111)
    ax.imshow(img, cmap='gray')
    plt.show()

img=cv2.imread('DATA/sudoku.jpg',0)
display_image(img)
print(img.shape)
###SOBEL OPERATORS
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
display_image(sobelx)
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
display_image(sobely)

blended=cv2.addWeighted(src1=sobelx,alpha=0.5,src2=sobely,beta=0.5,gamma=0)
display_image(blended)
ret,thres=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
display_image(thres)

kernel=np.ones((4,4),np.uint8)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
display_image(gradient)