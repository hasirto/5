for i in range(1,20):
    if (i%3==0 and i%5==0):
        print(i,"hem 5'e hemi de 3e bölünüyor")
    if i%3!=0 and i%5==0:
        print(i,"3e bölünmez 5e bölünür")
    if i%3==0 and i%5!=0:
        print(i,"3e bölünür 5e bölünmez")