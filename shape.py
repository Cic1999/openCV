import cv2
img = cv2.imread("./image/text.jpg",cv2.IMREAD_COLOR)
print(img.shape , img.size)
img[10:50,20:50] =[200,40,70]
img[60:100,40:70] =[100,100,80]
roi1 = img[10:50,20:50]
roi2 = img[60:100,40:70]

for i in range(10):
    if i == 0:

        cv2.imshow('text',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows
    else:
        