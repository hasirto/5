kelime =input("bir kelime giriniz")
a = 0#sesli harfleri saymak için sayaca 0 yazıyoruz
b = 0
c = 0
d = 0
sesli = "AEIOUÖUÜİaeıioöuü"#sesli harflerin olduğu değişken
sessiz = "bcçdfgğhjklmnprsştyz"
boşluk = " "
for harf in kelime:#kelimenin içinde harfleri ara
    if harf in sesli:#girilen kelimedeki sesli harflerle işlem yap
        a=a+ 1   #harfin içinde ne kadar sesli harf varsa a sayacı ile say
    if harf in boşluk:
        b += 1
    if harf in sessiz:
        c += 1
print("sesli harflerin sayısı:",a," sessiz harflerin sayısı:",c)
print("boşluk sayısı:",b)
print(kelime.isupper())
