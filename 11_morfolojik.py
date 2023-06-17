import cv2
import numpy as np
import matplotlib.pyplot as plt

#resmi içe aktar
img=cv2.imread("datai_team.jpg",0)
plt.figure()
plt.axis("off")
plt.title("orijinal")
plt.imshow(img,cmap="gray")

#erozyon
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 1) 
# iteration = 1 demek bunu 1 kere erozyona uğrat demek
plt.figure()
plt.axis("off")
plt.title("Erozyon")
plt.imshow(result, cmap="gray")

#genişleme dilation
result2=cv2.dilate(img,kernel,iterations = 1)
plt.figure()
plt.axis("off")
plt.title("Genisleme")
plt.imshow(result2, cmap="gray")


#açılma=gürültüyü(beyaz) azaltmak için kullanılır

#beyaz gürültü oluşturuldu
whiteNoise=np.random.randint(0,2,size=img.shape[:2])
whiteNoise=whiteNoise*255
plt.figure()
plt.axis("off")
plt.title("beyaz gürültü")
plt.imshow(whiteNoise, cmap="gray")

#beyaz gürültüyü orijinal resme ekledik
noise_img=whiteNoise+img
plt.figure()
plt.axis("off")
plt.title("beyaz gürültülü resim")
plt.imshow(noise_img, cmap="gray")

#açılma 
opening=cv2.morphologyEx(noise_img.astype(np.float32),cv2.MORPH_OPEN,kernel)
plt.figure()
plt.axis("off")
plt.title("açılmalı resim")
plt.imshow(opening, cmap="gray")


#kapatma (açılmanın tersi)

#black noise oluşturuldu
blackNoise=np.random.randint(0,2,size=img.shape[:2])
blackNoise=blackNoise*-255
plt.figure()
plt.axis("off")
plt.title("siyah gürültü")
plt.imshow(blackNoise, cmap="gray")

#black gürültüyü orijinal resme ekledik
black_noise_img=blackNoise+img
black_noise_img[black_noise_img<=-255]=0
plt.figure()
plt.axis("off")
plt.title("siyah gürültülü resim")
plt.imshow(black_noise_img, cmap="gray")

#kapatma(black noisden kurtulcaz)
closing=cv2.morphologyEx(black_noise_img.astype(np.float32),cv2.MORPH_CLOSE,kernel)
plt.figure()
plt.axis("off")
plt.title("kapama resim")
plt.imshow(closing, cmap="gray")
