import cv2
import numpy as np
from matplotlib import pyplot as plt


img =cv2.imread('./image/car.jpg')
img = cv2.resize(img,(600,400))
img1 = cv2.GaussianBlur(img,(13,13),0)
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
edges = cv2.Canny(gray,42,223)
c,h = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for cnt in c:
    if cv2.contourArea(cnt) > 1000:
        #draw = cv2.drawContours(img,cnt,-1,(0,255,0),2)
        length = cv2.arcLength(cnt,True)
        epsilon = 0.0001*length  #數字越小 畫的線就準
        approx =cv2.approxPolyDP(cnt,epsilon,True)
        draw = cv2.drawContours(img,approx,-1,(0,255,0),2)
        cv2.polylines(img,[approx],True,(0,255,0),2)

print(cv2.moments(c[8]))

cv2.imshow('canny',edges)
cv2.imshow('contour',draw)
cv2.waitKey(0)
cv2.destroyAllWindows()