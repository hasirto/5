anahtar = 1
while anahtar == 1:
    liste = {"a": "o","i": "o","e": "o","ş": "s"}
    metin = input("metni giriniz: ")
    for harf in liste:
        metin = metin.replace(harf, liste[harf])
    print(metin)
    anahtar=0