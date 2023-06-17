import cv2
from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt

#siyah & beyaz
# def convert_image_to_black_and_white(image):
#     original_image=cv2.imread("umut.png")
#     gray_image=cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
#     (thresh, blackAndWhiteImage) = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
#     return blackAndWhiteImage

# #gri
# def convert_image_to_gray(image):
#     gray_image=cv2.imread("umut.png",0)
#     return gray_image

# #resized
# def convert_to_resized(image):
#     resize=cv2.resize(image,(150,150))
#     return resize


# #birleştirme

# #horizol
# def horizontal_stack(image):
#     hor=np.hstack((image,image))
#     return hor

# #vertical
# def vertical_stack(image):
#     ver=np.vstack((image,image))
#     return ver

# convert_image_to_black_and_white_image=convert_image_to_black_and_white(image)
# plt.figure()
# plt.imshow(convert_image_to_black_and_white_image)



