#自适应阈值
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./image/test13.jpg', 0)
img = cv2.medianBlur(img, 5)  # 中值滤波

ret, th1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY) #100的數值會影響Global Thresholding呈現的畫面
# 11 为 Block size, 2 为 C 值
#cv.ADAPTIVE_THRESH_MEAN_C 平均值
#cv.ADAPTIVE_THRESH_GAUSSIAN_C 附近值得加權和
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)  #15是Block size  越大照片中的雜質越明顯 #但如果C值越大 也會讓雜質比較少
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 10) 
titles = ['Original Image',
          'Global Thresholding (v = 100)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
for i in range(4):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray') #plt.subplot(row, cols, index)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
