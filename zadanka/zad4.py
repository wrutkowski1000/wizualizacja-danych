class NaZakupy:
  nazwa_produktu = "pusta"
  ilosc = 0
  jednostka_miary = "brak"
  cena = 0

  def __init__(self, nazwa, ilo, jednostka, cen):
      self.nazwa_produktu = nazwa
      self.ilosc = ilo
      self.jednostka_miary = jednostka
      self.cena = cen

  def wyswietl_produkt(self):
      print(self.nazwa_produktu, " ", self.ilosc," cena za", self.jednostka_miary, ":", self.cena, "zl")

  def ile_produktu(self):
      print(self.ilosc, self.jednostka_miary)

  def ile_kosztuje(self):
      print(self.ilosc*self.cena)

marchewka = NaZakupy("marchewka", 10, "kg", 4.00)
marchewka.wyswietl_produkt()
marchewka.ile_produktu()
marchewka.ile_kosztuje()