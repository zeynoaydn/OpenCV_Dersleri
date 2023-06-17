import cv2

img=cv2.imread("Lenna.png")
print("resim boyutu:",img.shape)
cv2.imshow("deneme",img)

#resized
img_resize=cv2.resize(img,(150,150))
# print("resize image shape:",img_resize.shape)
cv2.imshow("img resized:",img_resize)

#kırpma
img_cropped=img[:200,:300]
cv2.imshow("kirpik resim",img_cropped)


cv2.waitKey(0)
cv2.destroyAllWindows()
