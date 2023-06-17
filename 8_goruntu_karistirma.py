import cv2
import matplotlib.pyplot as plt

#karıştırma
img1=cv2.imread("sky.jpg")
img1=cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)

img2=cv2.imread("nature.jpg")
img2=cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print(img1.shape)
print(img2.shape)

img1=cv2.resize(img1,(3200,2000))
print(img1.shape)

img2=cv2.resize(img2,(3200,2000))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

#karıştırılmış resim=alpha*img1+beta*img2
#alpha ve beta değerlerini değiştirebilirsin
blended=cv2.addWeighted(src1=img1,alpha=0.5,src2=img2,beta=0.5,gamma=0)
plt.figure()
plt.imshow(blended)

# cv2.waitKey(0)
# cv2.destroyAllWindows()