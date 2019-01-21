class Iterator:
    def __iter__(self):
        self.licznik=0
        return self    #skoro jesteśmy obiektem iterowalnym, to zwracamy siebie, bo obiekt iterowalny powinien mieć metodę next

    def __next__(self):
        if self.licznik > 10:
            raise StopIteration   #podnosimy StopIteration
        liczba = self.licznik
        self.licznik += 1
        return liczba

for i in Iterator():
    print(i)