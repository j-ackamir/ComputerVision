import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


pic = Image.open('DATA/00-puppy.jpg')
pic_arr = np.asarray(pic)

plt.imshow(pic_arr)
plt.title('Original Image')
plt.show()


pic_red = pic_arr.copy()
pic_red[:, :, 1:] = 0


plt.imshow(pic_red)
plt.title('Image with Only Red Channel')
plt.show()




