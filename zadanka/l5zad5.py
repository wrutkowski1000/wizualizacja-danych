class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

osoba1 = Menadzer("Krzysztof", "Ibisz", 100)
osoba2 = Pracownik("Karol","Krawczyk", 1000000)
print(isinstance(osoba2, Pracownik))
print(isinstance(osoba1, Pracownik))
print(isinstance(osoba1, Menadzer))
print(isinstance(osoba2, Menadzer))