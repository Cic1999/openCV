#平移
import cv2
import numpy as np
img =  cv2.imread('./image/img1.jpg')
img = cv2.resize(img,(700,500))
rows,cols,channel = img.shape
#M = np.float32([[1,0,100],[0,1,50]])  #左平移100 下平移50
#M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)  #旋轉90
#dst = cv2.warpAffine(img,M,(cols,rows))  #平移
#dst = cv2.warpAffine(img,M,(rows,cols))   #旋轉
#dst = cv2.flip(img,-1) #上下左右翻轉
#dst = cv2.flip(img,1) #左右翻轉
#dst = cv2.flip(img,0) #上下翻轉
M = cv2.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),45,2)  
dst = cv2.warpAffine(img,M,(rows*2,cols*2)) #14 15 旋轉後翻轉

cv2.imshow('dst',dst)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()