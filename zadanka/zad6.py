class Slowa:
    global tabslow
    def __init__(self, slowo1, slowo2):
        self.tabslow = [slowo1, slowo2]

    def palindrom(self, slowo):
        pal = 0
        for i in range(len(slowo)):
            if slowo[i] == slowo[len(slowo)-i-1]:
                pal = 1
            else:
                pal = 0

        if pal == 1:
            print("Jest palindromem")
        else:
            print("Nie jest palindromem")

slowka = Slowa("skkrrrrr", "kajak");
slowka.palindrom(slowka.tabslow[1])