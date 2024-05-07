import numpy as np
import matplotlib.pyplot as plt
import cv2

######TEMPLATE MATCHING########

full=cv2.imread('DATA/sammy.jpg')
full=cv2.cvtColor(full,cv2.COLOR_BGR2RGB)
plt.imshow(full)
# plt.show()
face=cv2.imread('DATA/sammy_face.jpg')
face=cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
plt.imshow(face)
# plt.show()

full_copy=full.copy()
method=cv2.TM_CCOEFF
res=cv2.matchTemplate(full_copy,face,method)

min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
top_left=max_loc
height,width,channels=face.shape
bottom_right=(top_left[0]+width,top_left[1]+height)

cv2.rectangle(full_copy,top_left,bottom_right,(255,0,0),10) 
plt.imshow(full_copy)
#plt.show()


######HARRIS CORNER DETECTION########

flat_chess=cv2.imread('DATA/flat_chessboard.png')
flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
gray_flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)

real_chess=cv2.imread('DATA/real_chessboard.jpg')
real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
gray_real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)

GRAY=np.float32(gray_real_chess)

dst=cv2.cornerHarris(GRAY,blockSize=2,ksize=3,k=0.04)
dst=cv2.dilate(dst,None)

real_chess[dst>0.01*dst.max()]=[255,0,0]
plt.imshow(real_chess)
#plt.show()

######SHI-TOMASI CORNER DETECTION########
flat_chess=cv2.imread('DATA/flat_chessboard.png')
flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2RGB)
gray_flat_chess=cv2.cvtColor(flat_chess,cv2.COLOR_BGR2GRAY)

real_chess=cv2.imread('DATA/real_chessboard.jpg')
real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2RGB)
gray_real_chess=cv2.cvtColor(real_chess,cv2.COLOR_BGR2GRAY)


corners=cv2.goodFeaturesToTrack(gray_real_chess,80,0.01,10)
corners=np.int0(corners)

for i in corners:
    x,y=i.ravel()
    cv2.circle(real_chess,(x,y),3,(255,0,0),-1)

plt.imshow(real_chess)
#plt.show()

######CANNY EDGE DETECTION########

img=cv2.imread('DATA/sammy_face.jpg')
img=cv2.blur(img,(5,5))
med=np.median(img)
lower=int(max(0,0.7*med))
upper=int(min(255,1.3*med))
edges=cv2.Canny(img,lower,upper)
plt.imshow(edges)
#plt.show()

######GRID DETECTION########
flat_chess=cv2.imread('DATA/flat_chessboard.png')
found,corners=cv2.findChessboardCorners(flat_chess,(7,7))
print(found)
cv2.drawChessboardCorners(flat_chess,(7,7),corners,found)
plt.imshow(flat_chess)
#plt.show()

dots=cv2.imread('DATA/dot_grid.png')
found,corners=cv2.findCirclesGrid(dots,(10,10),cv2.CALIB_CB_SYMMETRIC_GRID)
cv2.drawChessboardCorners(dots,(10,10),corners,found)
plt.imshow(dots)
#plt.show()

######GRID DETECTION########
img=cv2.imread('DATA/internal_external.png',0)
plt.imshow(img)
plt.show()
image,contours,hierarchy=cv2.findContours(img,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
external_contours=np.zeros(image.shape)
internal_contours=np.zeros(image.shape)
for i in range(len(contours)):

    if hierarchy [0][i][3]==-1:
        cv2.drawContours(external_contours,contours,i,255,-1)
    else:
       cv2.drawContours(internal_contours,contours,i,255,-1)

plt.imshow(external_contours)
plt.show()
plt.imshow(internal_contours)
plt.show()





