class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Employee(Osoba):     #Employee dziedziczy po Osoba
    def __init__(self, imie, nazwisko, stawka):
        #self.imie = imie      to jest niepotrzebne, bo jest dziedziczone po Osoba
        #self.nazwisko = nazwisko
        super().__init__(imie, nazwisko)    #potrzebne do dziedziczenia
        self.stawka = stawka
        self.godzin = 0  #nowy pracownik ma na początku przepracowane 0 godzin

    def register_time(self, czas_pracy):
       if czas_pracy >= 8:
           czas_pracy = (czas_pracy - 8)*2
           self.godzin += czas_pracy+8
       else:
           self.godzin += czas_pracy

    def pay_salary(self):
        wyplata = (self.stawka * self.godzin)
        self.godzin = 0.0
        return wyplata


# ZADANIE 7
class PremiumEmployee(Employee):

    def __init__(self, imie, nazwisko, stawka):
        super().__init__(imie, nazwisko, stawka)
        self.bonus = 0

    def give_bonus(self, kwota):
        self.bonus += kwota

    def Pay_Salary(self):
        old = super().pay_salary()
        return old + self.bonus


employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.register_time(10)    #8h + 2h nadgodzin
print(employee.pay_salary())  #1700 lub 1500 nie licząc nadgodzin

print(kopacz.pay_salary())