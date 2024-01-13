


import time
import random
import sys

class oyuncu():
    def __init__(self,isim,can=5,enerji=100):
        self.isim=isim
        self.darbe=0
        self.can=can
        self.enerji=enerji
    def mevcut(self):
        print(self.darbe)
        print(self.can)
        print(self.enerji)
    def saldir(self,rakip):
        print("bir saldiri gerceklesti")
        for i in range(10):
            time.sleep(.3)
            print('.',end='',flush=True)
        sonuc=self.saldirisonucu()
        if sonuc==0:

            print("kazanan yok")
        if sonuc==1:
            print("rakip darbelendi")
            self.darbele(rakip)
        if sonuc==2:
            print("darbe aldiniz")
            rakip.darbele(self)


    def saldirisonucu(self):
        return random.randint(0,2)
    def kac(self):
        print("kaciliyor")
        for i in range(10):
            time.sleep(3)
            print(flush=True)
            print("rakip sizi yakaladı")
    def darbele(self,darbelenen):
        darbelenen.darbe+=1
        darbelenen.enerji-=1
        if(darbelenen.darbe%5==0):
            darbelenen.can-=1
        if(darbelenen.can<1):
            darbelenen.enerji=0
            print("{} kazandi".format(self.isim))
            self.cik()
    def cik(self):
        print("cikilıyor")
        sys.exit()

siz=oyuncu('sevval')
rakip=oyuncu('gamze')

while True:
    print("suanda rakiple karsı karsıyasınız.Hamleler saldırmak için s,kac :k,cik :q",sep='\n')
    hamle=input('\n')
    if hamle=="s":
        siz.saldir(rakip)
        print("rakibinizin durumu")
        rakip.mevcut()
        print("sizin durumunuz")
        siz.mevcut()
    if hamle=="k":
        siz.kac()
    if hamle=="q":
        siz.cik()