import cv2

#讀圖
img = cv2.imread('../openCV/image/text.jpg',cv2.IMREAD_GRAYSCALE)
#秀圖
cv2.imshow('text',img)
#等待按鍵，關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()
#寫檔
cv2.imwrite('output.jpg',img)

