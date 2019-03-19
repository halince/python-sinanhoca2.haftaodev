def tahmin(a):
    sayac=0
    while True:
        sayi=int(input("aklınızdan 1 ile 100 arasında bir sayi tutunuz"))
        sayac=sayac+1
        if a==sayi:
            return sayac,"tane tahminde bulundunuz"
            break
x=int(input("kullanıcının tuttuğu sayi"))     
print(tahmin(x))
