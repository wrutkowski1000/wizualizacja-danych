class Ksztalty:
    # definicja konstruktora
    def __init__(self, x, y):
        # deklarujemy atrybuty
        # self wskazuje że chodzi o zmienne właśnie definiowanej klasy
        self.x=x
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x = x
        self.y = x
    def __add__(self, other):
        return Kwadrat(self.x + other.x)

    def __ge__(self, other):
        if self.x >= other.x:
            return 1
        else:
            return 0

    def __gt__(self, other):
        if self.x > other.x:
            return 1
        else:
            return 0

    def __le__(self, other):
        if self.x <= other.x:
            return 1
        else:
            return 0

    def __lt__(self, other):
        if self.x < other.x:
            return 1
        else:
            return 0


k1 = Kwadrat(5)
k2 = Kwadrat(10)
k3 = k1 + k2

if k2 > k1:
    print(k3.x)
else:
    print("k2 musi byc wieksze")

