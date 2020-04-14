class Slowa:
    global tabslow
    def __init__(self, slowo1, slowo2):
        self.tabslow = [slowo1, slowo2]

    def palindrom(self, slowo):
        for i in int(len(slowo)):
            if slowo[i] == slowo[int(len(slowo))-i] and i == int(len(slowo)):
                print("Jest palindromem")
            else:
                print("Nie jest palindromem")

