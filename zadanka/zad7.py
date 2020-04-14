class Robal:
    def __init__(self, rx, ry, rkrok):
        self.x = rx
        self.y = ry
        self.krok = rkrok

    def __del__(self):
        print("Robak zdechl")

    def idz_w_gore(self, kroki):
        self.y = self.y + kroki * self.krok

    def idz_w_dol(self, kroki):
        self.y = self.y - kroki * self.krok

    def idz_w_lewo(self, kroki):
        self.x = self.x - kroki * self.krok

    def idz_w_prawo(self, kroki):
        self.x = self.x + kroki * self.krok

    def pokaz_gdzie_jestes(self) :
        print("x={}, y={}".format(self.x, self.y))

robal = Robal(1,2,5)
robal.pokaz_gdzie_jestes()
robal.idz_w_gore(5)
robal.idz_w_dol(3)
robal.idz_w_lewo(2)
robal.idz_w_prawo(1)
robal.pokaz_gdzie_jestes()
del(robal)