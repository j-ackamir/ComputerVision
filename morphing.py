import numpy as np
import matplotlib.pyplot as plt
import cv2

def load_image():
    blank_img=np.zeros((600,600))
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300),fontFace=font,fontScale=5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
    return blank_img

def display_img(img):
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
    plt.show()

img=load_image()
#display_img(img)

kernel=np.ones((5,5),np.uint8)
result=cv2.erode(img,kernel,iterations=5)
#display_img(result)

img=load_image()
white_noise=np.random.randint(low=0,high=2,size=(600,600))
white_noise=white_noise*255
img=img+white_noise
#display_img(img)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
#display_img(opening)

img=load_image()
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
display_img(gradient)


