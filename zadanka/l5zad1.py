class Material:

    def __init__(self, r, d, s):
        self.rodzaj = r
        self.dlugosc = d
        self.szerokosc = s

    def wyswietl_nazwe(self):
        print(self.rodzaj)

class Ubrania(Material):

    def __init__(self, r, d, s, roz, kolo, dla):
        self.rodzaj = r
        self.dlugosc = d
        self.szerokosc = s
        self.rozmiar = roz
        self.kolor = kolo
        self.dla_kogo = dla

    def wyswietl_dane(self):
        print("rozmiar: ",self.rozmiar, " , kolor: ", self.kolor, " , dla: ", self.dla_kogo);

class Sweter(Ubrania):

    def __init__(self, d, s, roz, kolo, dla, rswetra):
        self.rodzaj = "sweter"
        self.dlugosc = d
        self.szerokosc = s
        self.rozmiar = roz
        self.kolor = kolo
        self.dla_kogo = dla
        self.rodzaj_swetra = rswetra

    def wyswietl_dane(self):
        print("rozmiar: ", self.rozmiar, " , kolor: ", self.kolor, " , dla: ", self.dla_kogo, " rodzaj swetra: ", self.rodzaj_swetra);


ubranko = Sweter(10, 50, 15, "czarny", "dla mnie","bawelniany")
ubranko.wyswietl_dane()