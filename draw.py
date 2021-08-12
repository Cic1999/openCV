import cv2
import numpy 
img = cv2.imread('./image/img1.jpg')

cv2.line(img,(100,100),(300,300),(0,0,255),5) #畫線(圖片，位置，位置，顏色，寬度)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.rectangle(img,(200,100),(400,500),(0,255,255),5) #畫長方形(圖片，位置，位置，顏色，寬度)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.circle(img,(300,300),45,(205,200,220),-1) #畫圓形(圓心，半徑，顏色，寬度(若-1填滿))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.ellipse(img,(400,400),(150,300),0,0,180,255,-1) #畫圓形(圓心位置，軸的長度，旋轉角度，起點跟終點，寬度(若-1填滿))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows

#pts = numpy.array([[10,5],[20,30],[70,20],[50,10]], np.int32)  #畫多邊形 (4個點位置)
#pts = pts.reshape((-1,1,2))
#cv.polylines(img,[pts],True,(0,255,255)))
#cv2.imshow('img',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows

cv2.putText(img,"OpenCV",(100,100),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),3)
cv2.EMD
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows
