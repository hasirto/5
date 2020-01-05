while True:
    metin = input("bana bir seyler söyle")
    yeni_metin = "" #yeni metin

    for harf in metin:
        if harf == "a" or harf == "e" or harf == "i" or harf == "u" or harf == "ı":#eğer metinde bu harfler var ise
            yeni_metin = yeni_metin + "o"#girilen string değerindeki harfleri o ile değiştir yani ekle
        else:
            yeni_metin = yeni_metin + harf
    print(yeni_metin)
