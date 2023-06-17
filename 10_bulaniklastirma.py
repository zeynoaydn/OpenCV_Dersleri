import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.filterwarnings("ignore")

#blurring=detayı azaltır,gürültüyü engeller
img=cv2.imread("NYC.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.figure()
plt.axis("off")
plt.title("original")
plt.imshow(img)

#ortalama bulanıklaştırma yöntemi
dst2=cv2.blur(img,ksize=(3,3))  #kszie=kutu boyutu
plt.figure()
plt.axis("off")
plt.title("ortalama blur")
plt.imshow(dst2)

#gauss bulanıklaştırma yöntemi
gb=cv2.GaussianBlur(img,ksize=(3,3),sigmaX=7)
plt.figure()
plt.axis("off")
plt.title("gauss blur")
plt.imshow(gb)

#median bulanıklaştırma yöntemi
md=cv2.medianBlur(img,ksize=3)
plt.figure()
plt.axis("off")
plt.title("median blur")
plt.imshow(md)

#gürültü oluşturuyoruz
def guassianNoise(image):
    row,col,ch=image.shape
    mean=0
    varyans=0.05
    sigma=varyans**0.5
    
    gauss=np.random.normal(mean,sigma,(row,col,ch))
    gauss=gauss.reshape(row,col,ch)
    noisy=image+gauss
    
    return noisy

#gürültüyü eklemek için resmi normalize ediyoruz
img=cv2.imread("NYC.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)/255
plt.figure()
plt.axis("off")
plt.title("normalize resim")
plt.imshow(img)

#resme gürültü ekliyoruz
guassianNoiseImage=guassianNoise(img)
plt.figure()
plt.axis("off")
plt.title("gurultulu resim")
plt.imshow(guassianNoiseImage)

#gauss blur
gb2=cv2.GaussianBlur(guassianNoiseImage,ksize=(3,3),sigmaX=7)
plt.figure()
plt.axis("off")
plt.title("with gauss blur")
plt.imshow(gb2)

#salt pepper oluşturuldu
def saltpepperNoise(image):
    row,col,ch=image.shape
    s_vs_p=0.5
    amount=0.004
    noisy=np.copy(image)
    
    #salt
    num_salt=np.ceil(amount*image.size*s_vs_p)
    coords=[np.random.randint(0,i-1,int(num_salt))for i in image.shape]
    noisy[coords]=1
    
    #pepper
    num_pepper=np.ceil(amount*image.size*(1-s_vs_p))
    coords=[np.random.randint(0,i-1,int(num_pepper))for i in image.shape]
    noisy[coords]=0
    
    return noisy

#resme salt pepper eklendi
saltpepperNoiseImage=saltpepperNoise(img)
plt.figure()
plt.axis("off")
plt.title("sp image")
plt.imshow(saltpepperNoiseImage)

#resimden salt pepper gürültüsü eklendi
md2=cv2.medianBlur(saltpepperNoiseImage.astype(np.float32),ksize=3)
plt.figure()
plt.axis("off")
plt.title("with median blur")
plt.imshow(md2)