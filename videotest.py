import cv2
import time

# cap=cv2.VideoCapture(0)
# width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
# height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# writer=cv2.VideoWriter('myvideo2.mp4',cv2.VideoWriter_fourcc(*'DIVX'),20,(int(width),int(height)))

# #while True:
#     # ret,frame=cap.read()
#     # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     # gray=cv2.merge([gray,gray,gray])
#     # gray=cv2.flip(gray,-1)
#     # print(gray.shape)
#     # writer.write(gray)
#     # cv2.imshow('frame',gray)
#     # if cv2.waitKey(1) & 0xFF==ord('q'):
#     #     break

# cap.release()
# writer.release()
# cv2.destroyAllWindows()


cap=cv2.VideoCapture('myvideo2.mp4')

if cap.isOpened()==False:
    print('ERROR FILE NOT FOUND OR WRONG CODEC USED!')

while cap.isOpened():
    
    ret,frame=cap.read()

    if ret==True:
        time.sleep(1/20)
        cv2.imshow('frame',frame)
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    else:
        break
