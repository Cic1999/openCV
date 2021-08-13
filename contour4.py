import cv2
import numpy as np
from matplotlib import pyplot as plt

font = cv2.FONT_HERSHEY_SIMPLEX  # 设置字体样式


img = cv2.imread('./image/car.jpg')
img = cv2.resize(img,(600,400))
img1 = cv2.GaussianBlur(img,(13,13),0)
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
edges = cv2.Canny(gray,42,223)
c,h = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cnt1 =c[8]
draw = cv2.drawContours(img,cnt1,-1,(0,255,0),2)
cnt2 =c[14]
draw = cv2.drawContours(img,cnt2,-1,(0,255,0),2)
cnt3 =c[24]
draw = cv2.drawContours(img,cnt3,-1,(0,255,0),2)
print(cv2.matchShapes(cnt1,cnt2,1,0.0))
print(cv2.matchShapes(cnt2,cnt3,1,0.0)) #計算出來的值越小 代表相似
cv2.imshow('canny',edges)
cv2.imshow('contour',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
