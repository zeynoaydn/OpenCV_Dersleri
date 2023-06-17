from PIL import Image
img = Image.open(r"intern.jpg") 
img.show()
img

from PIL import Image
img = Image.open(r"intern.jpg") 
print(img.format)
#This will return image format
print(img.size)
#This will return image dimension
print(img.mode)
#This will return image color mode

from PIL import Image
img = Image.open(r"intern.jpg") 
rotated_img = img.rotate(270)
rotated_img.show()

from PIL import Image  
imageObject = Image.open(r"intern.jpg")   
#Perform a flip of left and right  
flipImg = imageObject.transpose(Image.FLIP_LEFT_RIGHT)  
flipImg.show()

from PIL import Image  
imageObject = Image.open(r"sky.jpg")   
#Perform a flip of left and right  
flipImg = imageObject.transpose(Image.FLIP_TOP_BOTTOM)  
flipImg.show()

from PIL import Image  
imageObject = Image.open(r"sky.jpg")   
#Perform a flip of left and right  
flipImg = imageObject.transpose(Image.ROTATE_90)  
flipImg.show()

# from PIL import Image
# img = Image.open(r"intern.jpg") 
# r_img = img.resize(64, 64)
# r_img.show()

from PIL import Image, ImageDraw 
img = Image.open(r"intern.jpg") 
d1 = ImageDraw.Draw(img)  
d1.text((100, 200), "Hello", fill=(255, 255, 0))  
img.show() 
img

from PIL import Image, ImageFilter  
Original_Image =Image.open(r"intern.jpg") 
Original_Image.show()    
  
#Applying Simple blur function  
blur_Image = Original_Image.filter(ImageFilter.BLUR)  
blur_Image.show()  

#Applying Box blur function  
blur_Image = Original_Image.filter(ImageFilter.BoxBlur(radius))  
blur_Image.show() 
#Radius can be from 0 to 1

#Applying Gaussian blur
blur_Image = Original_Image.filter(ImageFilter.GaussianBlur(6))  
blur_Image.show()

