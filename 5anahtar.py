print("""
Yapmak istediğiniz işlemi seçin:
1:Toplama
2:Cikarma
3:Bölme
4:Carpma
5:karesini ALma
6:Karekök
NOT: Çıkmak (q)
""")

anahtar = "acik"
while anahtar == "acik":
    islem = input("Seçiminiz : ")

    if islem == "q":
        print("cikiliyor...")
        anahtar = "kapalı"


    elif islem == "1":
        sayi1 = int(input("birinci sayiyi gir :"))
        sayi2 = int(input("ikinci sayiyi gir :"))
        print("sonucunuz :", sayi1 + sayi2)

    elif islem == "2":
        print("cikarma yapacaksın")

    elif islem == "3":
        print("bölme yapacaksın")

    elif islem == "4":
        print("carpma yapacaksın")

    elif islem == "5":
        print("karesini alacaksın")

    elif islem == "6":
        print("karekök alaacksın")