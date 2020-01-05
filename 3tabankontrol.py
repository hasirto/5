s1=int(input("taban değeri ver: "))
s2=int(input("tavan değeri ver: "))
b1=int(input("bölümü kontrol edilecek ilk sayıyı ver :"))
b2=int(input("bölümü kontrol edilecek ikinci sayıyı ver: "))
for i in range(s1,s2):
    if i%b1==0 and i%b2==0:
        print(i,"sayisi hem",b1,"e hem de",b2,"e bölünür")

    if i%b1!=0 and i%b2==0:
        print(i,"sayisi ",b1,"e bölünmez ",b2,"e bölünür")

    if i%b1==0 and i%b2!=0:
        print(i,"sayisi ",b1,"e bölünür ",b2,"e bölünmez")