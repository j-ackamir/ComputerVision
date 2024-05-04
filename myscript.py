import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


pic = Image.open('DATA/00-puppy.jpg')
pic_arr = np.asarray(pic)

plt.imshow(pic_arr)
plt.title('Original Image')
plt.show()


pic_copy = pic_arr.copy()
pic_copy2=pic_arr.copy()
pic_copy[:,:,1]=0
pic_copy[:,:,2]=0
pic_red=pic_copy2[:,:,0]




plt.imshow(pic_copy, cmap='gray')
plt.title('Image with Only Red Channel')
plt.show()

plt.imshow(pic_red, cmap='gray')
plt.title('Image with Only Red Channel')
plt.show()








