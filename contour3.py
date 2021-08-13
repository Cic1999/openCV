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
cnt =c[8]

'''# 長方形
x, y, w, h = cv2.boundingRect(cnt)
area = cv2.contourArea(cnt)
aspect_ratio = float(w)/h  # 长宽比
rect_area = w*h
extent = float(area)/rect_area  # 轮廓面积与边界矩形面积的比。
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area  # 轮廓面积与凸包面积的比。
cv2.rectangle(img1, (x, y), (x+w, y+h), (0, 255, 0), 2)
text1 = 'Aspect Ration: ' + str(round(aspect_ratio, 4))
text2 = 'Extent:  ' + str(round(extent, 4))
text3 = 'Solidity: ' + str(round(solidity, 4))
cv2.putText(img1, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img1, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img1, text3, (10, 90), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
'''

# 橢圓
ellipse = cv2.fitEllipse(cnt)
(x, y), (a, b), angle = cv2.fitEllipse(cnt)
cv2.ellipse(img, ellipse, (0, 255, 0), 2)
text1 = 'x: ' + str(int(x)) + ' y: ' + str(int(y))
text2 = 'a:  ' + str(int(a)) + ' b:  ' + str(int(b))
text3 = 'angle: ' + str(round(angle, 2))
cv2.putText(img, text1, (10, 30), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img, text2, (10, 60), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.putText(img, text3, (10, 90), font, 0.5, (0, 255, 0), 1, cv2.LINE_AA, 0)
cv2.imshow('canny',edges)
cv2.imshow('contour',img)
cv2.waitKey(0)
cv2.destroyAllWindows()