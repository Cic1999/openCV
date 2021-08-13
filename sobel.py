
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./image/img2.png',0)
roi = img[144:500,560:800]

#sobelx = cv2.Sobel(roi,cv2.CV_8U,1,0,ksize=1)  #ksize=3 的值越小顯示越清楚 不能偶數
#sobely = cv2.Sobel(roi,cv2.CV_8U,0,1,ksize=1)
sobelx = cv2.Sobel(roi,cv2.CV_64F,1,0,ksize=1) #用64F 再轉化8U 可以把線條抓得更精確
sobelx = cv2.convertScaleAbs(sobelx)  #convertScaleAbs 直接做轉換
sobely = cv2.Sobel(roi,cv2.CV_64F,0,1,ksize=1)
sobely = cv2.convertScaleAbs(sobely)

#把 sobelx 和 sobely 兩張圖各別0.5加起來 
sobel = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)
#把 sobelx 和 sobely 兩張圖直接加起來 
sobel1 = cv2.add(sobelx,sobely)
cv2.imshow('roi',roi)
cv2.imshow('sobelx',sobelx)
cv2.imshow('sobely',sobely)
cv2.imshow('sobel',sobel)
cv2.imshow('sobel ADD',sobel1)
cv2.waitKey(0)
cv2.destroyAllWindows()
