class Robaczek :
    def init (self, rx, ry, rkrok):
        self.x = rx
        self.y = ry
        self.krok = rkrok
    def idz_w_gore(self, ile_krokow):
        self.y = self.y + ile_krokow * self.krok
    def idz_w_dol(self, ile_krokow):
        self.y = self.y - ile_krokow * self.krok
    def idz_w_lewo(self, ile_krokow):
        self.x = self.x - ile_krokow * self.krok
    def idz_w_prawo(self, ile_krokow):
        self.x = self.x + ile_krokow * self.krok

    def pokaz_gdzie_jestes(self) :
        print("x={}, y={}".format(self.x, self.y))

robal = Robaczek()
robal.idz_w_gore(3)
robal.idz_w_dol(1)
robal.idz_w_lewo(3)
robal.idz_w_prawo(1)
robal.pokaz_gdzie_jestes()