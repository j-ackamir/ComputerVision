import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread('DATA/00-puppy.jpg')
#img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#img=cv2.cvtColor(img,cv2.COLOR_BGR2HLS)
plt.imshow(img)
plt.show()
