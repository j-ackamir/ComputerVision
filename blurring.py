import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_img():
    img=cv2.imread('DATA/bricks.jpg').astype(np.float32)/255
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def display_img(img):
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111)
    ax.imshow(img)
    plt.show()

bricks=load_img()
#display_img(bricks)
gamma= 0.25
bricks=np.power(bricks,gamma)
#display_img(bricks)

img=load_img()
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img,text='bricks',org=(10,600),fontFace=font,fontScale=10,color=(255,0,0),thickness=4)
#display_img(img)

#kernel=np.ones((5,5),np.float32)/25
#dst=cv2.filter2D(img,-1,kernel)
#display_img(dst)
blurred=cv2.blur(img,(5,5)) 
blurred=cv2.GaussianBlur(img,(5,5),10)
blurred=cv2.medianBlur(img,5)
#display_img(blurred)

img2=cv2.imread('DATA/sammy_noise.jpg')
display_img(img2)
blurred=cv2.medianBlur(img2,5)
display_img(blurred)