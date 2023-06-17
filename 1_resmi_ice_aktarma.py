import cv2
# catImage=cv2.imread("kedi.jpg")
catImage=cv2.imread("kedi.jpg",0)
cv2.imshow("deneme",catImage)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

k=cv2.waitKey(0)
if k==27: #esc
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite("kedi_gray.jpg",catImage)
    cv2.destroyAllWindows()

# s tuşuna basıldığında kedi resminin gri hali dosyaya
# indirilir