import cv2
img = cv2.imread("./image/text.jpg",cv2.IMREAD_COLOR)
print(img.shape , img.size)
img[10:50,20:50] =[200,40,70]
roi = img[10:50,20:50]
img[60:100,40:70] = roi

cv2.imshow('text',img)
cv2.waitKey(0)
cv2.destroyAllWindows