
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('./image/test16.png')
img2 = cv2.imread('./image/test17.png') #原圖

kernel = np.ones((5, 5), np.float32)/25
kerne2 = np.ones((10, 10), np.float32)/100

#腐蝕
erosion = cv2.erode(img,kernel,iterations=1)  #iterations=1 指侵蝕幾次

#膨脹
dilation = cv2.dilate(img,kernel,iterations=1)

#開運算 先侵蝕後膨脹
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

#閉運算  先膨脹後侵蝕
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

#型態梯度  字型中空
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

#頂帽  开运算结果的差值
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

#黑帽  闭运算结果的差值
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


plt.subplot(241),plt.imshow(img),plt.title('Original')
plt.subplot(242),plt.imshow(erosion),plt.title('Erosion')
plt.subplot(243),plt.imshow(dilation),plt.title('Dilation')
plt.subplot(244),plt.imshow(opening),plt.title('Opening')
plt.subplot(245),plt.imshow(closing),plt.title('Closing')
plt.subplot(246),plt.imshow(gradient),plt.title('Gradient')
plt.subplot(247),plt.imshow(tophat),plt.title('Tophat')
plt.subplot(248),plt.imshow(blackhat),plt.title('Blackhat')
plt.show()