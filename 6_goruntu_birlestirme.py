import cv2
import numpy as np

#resmi içe aktarma
img=cv2.imread("Lenna.png")
cv2.imshow("orijinal",img)

hor=np.hstack((img,img))
cv2.imshow("horizontal",hor)

ver=np.vstack((img,img))
cv2.imshow("vertical",ver)

cv2.waitKey(0)
cv2.destroyAllWindows()