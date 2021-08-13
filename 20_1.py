import cv2
import numpy as np


# 圖像尺寸最好是2的整次幕(因為每次除1/2)
img = cv2.imread('./image/test6.jpg')
lower = cv2.pyrDown(img)
lower1 = cv2.pyrDown(lower)
upper = cv2.pyrUp(lower1)
upper1 = cv2.pyrUp(upper)

laplce = cv2.subtract(img,upper1) #subtract 相減


while (1):
    cv2.imshow('img',img)
    cv2.imshow('loewr',lower)
    cv2.imshow('lower1',lower1)
    cv2.imshow('upper',upper)
    cv2.imshow('upper1',upper1)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()