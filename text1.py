#Import only if not previously imported
import cv2
img = cv2.imread("./image/text.jpg",1)     #(flag = 0 or 1 or -1)

#Import only if not previously imported
import cv2
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Import only if not previously imported
import cv2
cv2.imwrite("imageTest",img)