class mojiterator:

    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index%2 == 0:
            return self.data[self.index]


nazwa = mojiterator("ABCDEFGHIJ")
n = iter(nazwa)
for i in range(0,9):
    print(next(n))