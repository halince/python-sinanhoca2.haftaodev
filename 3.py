toplam=0
sayac=0
while True:
    sayi=int(input("1 ile 100 arasında sayılar giriniz"))
    if sayi<=0 or sayi>100:
        print("1 ile 100 arasında bir sayı girmelisiniz" )
    elif sayi>50:
        toplam=toplam+sayi
    elif sayi<50:
        sayac=sayac+1
    elif sayi==50:
        print("girdiğiniz 50 den büyük sayıların toplamı=",toplam)
        print("girdiğiniz 50 den küçük saı adedi=",sayac)
        break
