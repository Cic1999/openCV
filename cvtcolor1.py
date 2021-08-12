#辨識圖片顏色 用6個Trackbar 抓更精確的顏色數值

import cv2 as cv
import numpy as np

def abc(x):
    pass

cv.namedWindow('res')
cv.createTrackbar('hmin','res',0,180,abc)
cv.createTrackbar('hmax','res',0,180,abc)
cv.createTrackbar('smin','res',0,255,abc)
cv.createTrackbar('smax','res',0,255,abc)
cv.createTrackbar('vmin','res',0,255,abc)
cv.createTrackbar('vmax','res',0,255,abc)
img = cv.imread('./image/img1.jpg')  #讀照片

cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    #_, frame = cap.read()  這個要取消掉
    frame = img #加這個
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hmin = cv.getTrackbarPos('hmin','res')  #Trackbar抓到的顏色
    hmax = cv.getTrackbarPos('hmax','res')  #Trackbar抓到的顏色
    smin = cv.getTrackbarPos('smin','res')  #Trackbar抓到的顏色
    smax = cv.getTrackbarPos('smax','res')
    vmin = cv.getTrackbarPos('vmin','res')  #Trackbar抓到的顏色
    vmax = cv.getTrackbarPos('vmax','res')
    # define range of blue color in HSV
    lower_blue = np.array([hmin,smin,vmin])  #np.array([顏色範圍, , ])  可以上網查看顏色範圍 
    upper_blue = np.array([hmax,smax,vmax]) #若用Trackbar np.array([放Trackbar抓到的顏色, , ]) 
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
