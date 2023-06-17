import cv2
import numpy as np

#resim olusturma
img=np.zeros((512,512,3),np.uint8) #siyyah bir resim
print(img.shape)

cv2.imshow("siyah",img)

#çizgi
#(resim,başlangıç noktası,bitiş noktası,renk,çizgi kalınlığı)
# cv2.line(img,(0,0),(512,512),(0,255,0),3) 
cv2.line(img,(100,100),(232,122),(0,255,0),3)
#0,0 sol üst köşe
cv2.imshow("cizgi",img)

#dikdörtgn
#(resim,başlangıç,bitiş,renk)
# cv2.rectangle(img,(0,0),(256,256),(255,0,0))
cv2.rectangle(img,(0,0),(256,256),(255,0,0),cv2.FILLED)
cv2.imshow("dikdortgen",img)

#cember
#(resim,merkez,yarıçap,renk)
cv2.circle(img,(300,300),45,(0,0,255))
cv2.imshow("cember",img)

#metin
#(resim,başlangıç,font,kalınlık,renk)
cv2.putText(img,"merhaba dünya",(350,234),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("metin",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
