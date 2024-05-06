import numpy as np
import cv2

import matplotlib.pyplot as plt

blank_img=np.zeros(shape=(512,512,3),dtype=np.uint8) 
plt.imshow(blank_img)
#plt.show()
cv2.rectangle(blank_img,pt1=(100,100),pt2=(300,400),color=(0,0,255),thickness=10)
plt.imshow(blank_img)
plt.show()

cv2.circle(blank_img,center=(200,200),radius=50,color=(255,0,0),thickness=-5)
cv2.line(blank_img, pt1=(0,0),pt2=(512,512),color=(102,255,255),thickness=5)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(blank_img,'Hello',org=(10,400),fontFace=font, fontScale=4, color=(255,255,255))
plt.imshow(blank_img)
#plt.show()

blank=np.zeros(shape=(512,512,3),dtype=np.uint8) 
vertices=np.array([[100,100],[200,200],[400,300],[200,400]], dtype=np.int32)
#print(vertices.shape)
pts= vertices.reshape((-1,1,2))
#print(vertices)
cv2.fillPoly(blank,[pts], color=(255,0,0))
plt.imshow(blank)
plt.show()

