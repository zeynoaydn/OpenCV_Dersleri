import cv2
import numpy as np

#içe aktarma
img=cv2.imread("kart.png")
cv2.imshow("resim",img)

width=400
height=500

pts1=np.float32([[230,1],[1,472],[540,150],[338,617]])
pts2=np.float32([[0,0],[0,height],[width,0],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)
#matrix=rotasyon adresi

#cevirme işlemi
img_output=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("donusturulmus",img_output)

cv2.waitKey(0)
cv2.destroyAllWindows()