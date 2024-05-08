import numpy as np
import matplotlib.pyplot as plt
import cv2

#corners_params=dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7) 
#lk_params=dict(winSize=(15,15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

cap = cv2.VideoCapture(0)
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

prevPts = cv2.goodFeaturesToTrack(old_gray,None,10,0.3,7,7)

mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, prevPts, None, winSize=(15,15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
    

