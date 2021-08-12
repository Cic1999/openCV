#简单阈值法 
#cv.THRESH_BINARY
#cv.THRESH_BINARY_INV
#cv.THRESH_TRUNC
#cv.THRESH_TOZERO
#cv.THRESH_TOZERO_INV
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./image/img1.jpg', 0)
ret, thresh1 = cv2.threshold(img, 167, 255, cv2.THRESH_BINARY)  # cv.threshold(圖像，灰度，阈值 )
ret, thresh2 = cv2.threshold(img, 167, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 167, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 167, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 167, 255, cv2.THRESH_TOZERO_INV)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')  #plt.subplot(row,cols,index)
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
