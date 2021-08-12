#Otsu二值化
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./image/test14.jpg', 0)
# global thresholding 全國閥值
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Otsu's thresholding  Otsu閥值
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering 經過高斯濾波的Otsu閥值
# （9,9）为高斯核的大小，8 为标准差
blur = cv2.GaussianBlur(img, (15, 15), 0)   #(5,5)裡面的值不可為偶數
# 阈值一定要设为 0！
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# plot all the images and their histograms 畫出所有的圖像和他們的閥值
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)', 'Original Noisy Image',
          'Histogram', "Otsu's Thresholding", 'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]
# 这里使用了 pyplot 中画直方图的方法，plt.hist, 要注意的是它的参数是一维数组
# 所以这里使用了（numpy）ravel 方法，将多维数组转换成一维，也可以使用 flatten 方法
# ndarray.flat 1-D iterator over an array.
# ndarray.flatten 1-D array copy of the elements of an array in row-major order
for i in range(3):
    plt.subplot(3, 3, i*3+1), plt.imshow(images[i*3], 'gray') #26、27 顯示直的原圖
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+2), plt.hist(images[i*3].ravel(), 256) #28、29 顯示高峰的藍圖
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i*3+3), plt.imshow(images[i*3+2], 'gray') #30、31 以127作為顏色呈現的值
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()
