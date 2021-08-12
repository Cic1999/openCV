#雙邊滤波練習
import cv2
from matplotlib import pyplot as plt
img = cv2.imread("./image/test15.jpg")
img = cv2.resize(img,(600,400))
bila = cv2.bilateralFilter(img,5,200,200)
bila2 = cv2.bilateralFilter(img,5,200,10)


plt.subplot(131),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB)),plt.title('Original')
plt.subplot(132),plt.imshow(cv2.cvtColor(bila,cv2.COLOR_BGR2RGB)),plt.title('bila')
plt.subplot(133),plt.imshow(cv2.cvtColor(bila2,cv2.COLOR_BGR2RGB)),plt.title('bila2')
plt.show()
#cv2.imshow("img",img)
#cv2.imshow("bila",bila)
#cv2.imshow("bila2",bila2)
#cv2.waitKey(0)
#cv2.destroyAllWindows()