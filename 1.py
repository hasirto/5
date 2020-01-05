a=int(input("başlangıç sayısı: "))
b=int(input("bitiş sayısı: "))
for i in range(a,b):
    i=i+10
    if i %2!=0:
        print(i,"sayı çift değildir")
    if i%3!=0 and i%9!=0:
        print(i,"hem 3 e hemde 9 a bölünemez")
