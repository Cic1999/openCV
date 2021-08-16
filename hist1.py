import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./image/img1.jpg',0)
mask =np.zeros(img.shape[:2],np.uint8)
mask[50:380, 840:1070] = 255 #框起來
masked_img = cv2.bitwise_and(img, img, mask=mask)  #合起來
hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
cv2.imshow("hist_full",mask)
#cv2.imshow("hist_mask",hist_mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.subplot(221), plt.imshow(img, 'gray'), plt.title('Original')
plt.subplot(222), plt.imshow(mask, 'gray'), plt.title('Mask')
plt.subplot(223), plt.imshow(masked_img, 'gray'), plt.title('Masked')
plt.subplot(224), plt.plot(hist_full, label='original'),
plt.plot(hist_mask, label='masked'), plt.xlim([0, 256]),
plt.legend(loc=1), plt.title('Histogram')

plt.show()
