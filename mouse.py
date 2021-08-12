import cv2
def draw(event,x,y,flags,param):
     if event == cv2.EVENT_LBUTTONDBLCLK:
         cv2.circle(img,(x,y),100,(100,200,140),5)
img = cv2.imread("./image/img1.jpg")
cv2.namedWindow("image") 
cv2.setMouseCallback("image",draw)
while True:
    cv2.imshow("image",img)
    if cv2.waitKey(20)==27:
        break
cv2.destroyAllWindows()       