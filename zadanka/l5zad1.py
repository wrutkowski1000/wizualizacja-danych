class Material:

    rodzaj = ""
    dlugosc = 0
    szerokosc = 0

    def __init__(self, r, d, s):
        self.rodzaj = r
        self.dlugosc = d
        self.szerokosc = s

    def wyswietl_nazwe(self):
        print(self.rodzaj)

class Ubrania:
    rozmiar = 0
    kolor = ""
    dla_kogo = ""

    def wyswietl_dane(self):
        print("rozmiar: " ,self.rozmiar , " , kolor: " , self.kolor , " , dla: " , self.dla_kogo);

class Sweter:
    rodzaj_swetra = ""
    def wyswietl_dane(self):
        print("rozmiar: ", self.rozmiar, " , kolor: ", self.kolor, " , dla: ", self.dla_kogo, " rodzaj swetra: ", self.rodzaj_swetra);

        
ubranko = Ubrania()
ubranko.dla_kogo = "dla mnie"
ubranko.kolor = "czarny"
ubranko.rozmiar = 10
ubranko.wyswietl_dane()