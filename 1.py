import math
def ucgen(a,b):
    print("üçgenin alanı=",(a*b)/2,"çevresi=",a+b+math.sqrt(pow(a,2)+pow(b,2)))
def kare(a):
    print("karenin alanı=",a**2,"çevresi=",4*a)
def dikdortgen(a,b):
    print("dikdörtgenin alanı=",a*b,"çevresi=",2*(a+b))
print("seçiminizi yapınız üçgen için 1 kare için 2 dikdörtgen için 3 giriniz")
secim=input()
if secim=="1":
    a=int(input(""""alanını ve çevresini hesaplamak istediğiniz
    üçgenin dik kenarlarından birini giriniz"""))
    b=int(input("üçgenin diğer dik kenarını giriniz"))
    ucgen(a,b)
if secim=="2":
    x=int(input(""""alanını ve çevresini hesaplamak istediğiniz
    karenin  kenar uzunluğunu giriniz"""))
    kare(x)
if secim=="3":
    y=int(input(""""alanını ve çevresini hesaplamak istediğiniz
    dikdörtgenin  uzun kenarını giriniz"""))
    z=int(input(""""alanını ve çevresini hesaplamak istediğiniz
    dikdörtgenin  kısa kenarını giriniz"""))
    dikdortgen(z,y)
