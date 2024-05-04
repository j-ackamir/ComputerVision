import numpy as np
import cv2

import matplotlib.pyplot as plt

blank_img=np.zeros(shape=(512,512,3),dtype=np.uint8) 
plt.imshow(blank_img)
plt.show()
cv2.rectangle(blank_img,pt1=(100,100),pt2=(300,400),color=(0,0,255),thickness=10)
plt.imshow(blank_img)
plt.show()

cv2.circle(blank_img,center=(200,200),radius=50,color=(255,0,0),thickness=-5)
cv2.line(blank_img, pt1=(0,0),pt2=(512,512),color=(102,255,255),thickness=5)
plt.imshow(blank_img)
plt.show()

