import cv2 as cv
import numpy as np
# 4-9 Trackbar 若不要 可拉掉
def abc(x):
    pass

cv.namedWindow('res')
cv.createTrackbar('hmin','res',0,180,abc)
cv.createTrackbar('hmax','res',0,180,abc)

cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hmin = cv.getTrackbarPos('hmin','res')  #Trackbar抓到的顏色
    hmax = cv.getTrackbarPos('hmax','res')  #Trackbar抓到的顏色
    # define range of blue color in HSV
    lower_blue = np.array([hmin,50,50])  #np.array([顏色範圍, , ])  可以上網查看顏色範圍 
    upper_blue = np.array([hmax,255,255]) #若用Trackbar np.array([放Trackbar抓到的顏色, , ]) 
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
