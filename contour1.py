import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
    pass

#img = cv2.imread('./image/img1.jpg')
#img = cv2.resize(img,(600,400))

img =cv2.imread('./image/car.jpg')
img = cv2.resize(img,(600,400))
img1 = cv2.GaussianBlur(img,(13,13),0)
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)


cv2.namedWindow('image')
cv2.imshow('image',img)
#while True:
    

    #edges = cv2.Canny(gray,255,45)
    #c,h = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #draw = cv2.drawContours(img,c,-1,(0,255,0),3)
    #dst = cv2.bitwise_and(img,img,mask=edges)
    #cv2.imshow('canny',edges)
    #cv2.imshow('dst',draw)
    #if cv2.waitKey(1) == 27:
        #break
#cv2.destroyAllWindows()

edges = cv2.Canny(gray,255,45)
c,h = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#draw = cv2.drawContours(img,c,-1,(0,255,0),3)
draw = cv2.drawContours(img,c,8,(0,255,0),1)
print(len(c))
#print(c[0])
print(c[8])
plt.subplot(121),plt.imshow(edges, cmap='gray'), plt.title('edges')
plt.subplot(122),plt.imshow(draw, cmap='gray'), plt.title('draw')
plt.show()