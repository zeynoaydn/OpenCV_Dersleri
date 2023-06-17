# import cv2
# import matplotlib.pyplot as plt

# # resmi içe aktar
# img=cv2.imread("sky.jpg")
# img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #siyah beyaza çevrildi
# plt.figure()
# plt.imshow(img,cmap="gray")
# plt.axis("off") #eksenler kapatıldı
# plt.show()

# _,thresh_img=cv2.threshold(img,thresh=60,maxval=255,type=cv2.THRESH_BINARY)
# plt.figure()
# plt.imshow(thresh_img,cmap="gray")
# plt.axis("off")
# plt.show()

# thresh_img2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
# plt.figure()
# plt.imshow(thresh_img2,cmap="gray")
# plt.axis("off")
# plt.show()

import cv2

# resmi içe aktar
img=cv2.imread("sky.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #siyah beyaza çevrildi
cv2.imshow("Gray Image", img)
cv2.waitKey(0)

_,thresh_img=cv2.threshold(img,thresh=60,maxval=255,type=cv2.THRESH_BINARY)
cv2.imshow("Threshold Image", thresh_img)
cv2.waitKey(0)

thresh_img2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,8)
cv2.imshow("Adaptive Threshold Image", thresh_img2)
cv2.waitKey(0)

cv2.destroyAllWindows()
