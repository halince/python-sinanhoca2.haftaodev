def faktoriyel(a):
    sayac=1
    for i in range(1,a+1):
       sayac=sayac*(i)
    return sayac
sayi=int(input("faktoriyelini hesaplamak istediğiniz sayıyı giriniz"))
print(faktoriyel(sayi))
