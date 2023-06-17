import cv2

# capture
cap=cv2.VideoCapture(0)

width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)

# video kaydet
writer=cv2.VideoWriter("video_kaydi.mp4",cv2.VideoWriter_fourcc(*"DIVX"),20,(width,height))
# 20=her saniyede görülecek frame(resim) sayısı (ya da video hızı)
# fourcc=çerveleri sıkıştırmak için kullanılır

while True:
    ret,frame=cap.read()
    cv2.imshow("video",frame)
    
    # save (videoyu aynı zamanda kaydediyoruz)
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release() #cap tırı serbest bırakıyoruz
writer.release() #writer ı serbest bırakıyoruz (writer a yazma işlemi bitti diyooruz)
cv2.destroyAllWindows() #açık kalan pencereleri kapatıyoruz