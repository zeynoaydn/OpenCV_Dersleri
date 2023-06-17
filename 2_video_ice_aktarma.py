import cv2
import time

video_name="MOT17-04-DPM.mp4"

# içe aktarma
cap=cv2.VideoCapture(video_name)

print("genislik:",cap.get(3))
print("yukseklik:",cap.get(4))

if cap.isOpened()==False:
    print("hata")
else:
    print("hata yok")
    
while True:
    ret , frame =cap.read()
    if ret==True:
        time.sleep(0.01) #kullanılmazsa video çok hızlı akar
        cv2.imshow("video",frame)
    else:break
    
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break

cap.release() #stop capture
cv2.destroyAllWindows()