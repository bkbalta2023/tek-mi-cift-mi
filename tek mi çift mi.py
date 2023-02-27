print("""

Girdiğiniz sayıları tek ve çift oluşuna göre gruba ayırır.

Sonucu görmek için 'q' yazın.


""")




tek_sayilar = []
cift_sayilar =[]

while True:
    a = input("Sayı Giriniz: ")
    if a == "q":
        break
    else:
        a = int(a)
        if a % 2 ==0:
            cift_sayilar.append(a)
        else:
            tek_sayilar.append(a)
print("Girdiğiniz Çift Sayılar : ",cift_sayilar,"Girdiğiniz Tek Sayılar : ",tek_sayilar)

