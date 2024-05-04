import numpy as np
import matplotlib.pyplot as plt

import cv2
img = cv2.imread('DATA/00-puppy.jpg')
print(type(img))

img2=cv2.imread('wrong/path')
print(type(img2))

import numpy as np
import matplotlib.pyplot as plt

import cv2
img = cv2.imread('DATA/00-puppy.jpg')

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.title('Fixed Image')
plt.show()


img_gray=cv2.imread('DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)
print(img_gray.shape)
plt.imshow(img_gray, cmap='gray')
plt.show()

img_resized=cv2.resize(img,(1000,400))
plt.imshow(img_resized)
plt.show()

new_img=cv2.resize(img,(0,0),img,0.5,0.5)
new_img=cv2.flip(new_img,-1)
plt.imshow(new_img)
plt.show()
print(new_img.shape)

cv2.imwrite('totally_new.jpg',new_img)

fig = plt.figure(figsize=(10,8))
ax=fig.add_subplot(111)
ax.imshow(img)
plt.show()


