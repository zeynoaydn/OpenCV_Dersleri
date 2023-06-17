import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread("red_blue.jpg")
img_vis=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure(),
plt.imshow(img_vis)

# "print(img.shape)

# img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256]) 
# print(img_hist.shape)
# plt.figure()
# plt.plot(img_hist)

# color=("b","g","r")
# plt.figure()
# for i, c in enumerate(color):
#     hist=cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256]) 
#     plt.plot(hist,color=c)"
    
#histogram eşitleme(kontrast(karşıtlık) arttırma)
#bu sayede resim detaylarını öne çıkartabiliriz
img=cv2.imread("hist_equ.jpg",0)
plt.figure()
plt.imshow(img,cmap="gray")

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(img_hist)

eq_img = cv2.equalizeHist(img)
plt.figure()
plt.imshow(eq_img, cmap = "gray")

eq_img_hist = cv2.calcHist([eq_img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(eq_img_hist)