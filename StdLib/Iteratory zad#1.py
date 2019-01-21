#chcemy zrobic własnego range'a

class Iterator:
    def __init__(self, wartosc):
        print("Tworzę obiekt")
        self.wartosc = wartosc

    def __iter__(self):
        self.licznik = 0
        return self

    def __next__(self):
        if self.licznik > self.wartosc:
            raise StopIteration
        liczba = self.licznik
        self.licznik += 1
        return liczba

Counter = Iterator

for i in Counter(10):
    print(i)