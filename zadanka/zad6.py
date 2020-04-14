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

    def metagram(self, slowo1, slowo2):
        blad = 0
        if (len(slowo1) != len(slowo2)):
            print("Nie sa")
        else:
            for i in range(len(slowo1)):
                if slowo1[i] != slowo2[i]:
                    blad = blad + 1
        if blad <= 1:
            print("Sa metagramem")
        else:
            print("Nie sa")

slowka = Slowa("kujak", "kajak");
slowka.palindrom(slowka.tabslow[1])
slowka.metagram(slowka.tabslow[0], slowka.tabslow[1])