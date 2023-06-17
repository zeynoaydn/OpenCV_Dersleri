# f = open("a.txt", "r")
# print(f.read())
# print(f.readline())
# for x in f:
#   print(x)

# f = open("a.txt", "a")
# f.write("Artık dosyada daha çok veri var!")
# f.close()

# f = open("a.txt", "w")
# f.write("Hey, var olan içerik silindi!")
# f.close()

import os
if os.path.exists("a.txt"):
    os.remove("b.txt")
else:
    print("dosya bulunamadı")