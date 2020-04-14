class Slowa:
    global tabslow
    def __init__(self, slowa):
        self.tabslow = slowa

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
            print("Nie sa metagramem")
        else:
            for i in range(len(slowo1)):
                if slowo1[i] != slowo2[i]:
                    blad = blad + 1
            if blad <= 1:
                print("Sa metagramem")
            else:
                print("Nie sa metagramem")

    def anagram(self, slowo1, slowo2):
        jest = 0
        if (len(slowo1) != len(slowo2)):
            print("Nie sa anagramem")
        else:
            for i in range(len(slowo1)):
                help = 0
                for j in range(len(slowo1)):
                    if(slowo1[i]==slowo2[j]):
                        help = help + 1
                if help > 0:
                    jest = 1
                else:
                    jest = 0
            if jest == 1:
                print("Sa anagramem")
            else:
                print("Nie sa anagramem")

    def wyswietl(self):
        for i in range(len(self.tabslow)):
            print (self.tabslow[i])

slowka = Slowa(["kakrak", "kajak"]);
slowka.palindrom(slowka.tabslow[1])
slowka.metagram(slowka.tabslow[0], slowka.tabslow[1])
slowka.anagram(slowka.tabslow[0], slowka.tabslow[1])
slowka.wyswietl()