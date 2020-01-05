metin=input("metni gir kardeşim")
yeni_metin=""
for harf in metin:
    if harf not in yeni_metin and harf!=" ":
        yeni_metin=yeni_metin+harf

print(yeni_metin)
print(len(yeni_metin))