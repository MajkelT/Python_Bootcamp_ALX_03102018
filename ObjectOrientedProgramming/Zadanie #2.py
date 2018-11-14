class Employee():
    def __init__(self, imie, nazwisko, stawka):
        self.imie = imie
        self.nazwisko = nazwisko
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

employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.register_time(10)    #8h + 2h nadgodzin
print(employee.pay_salary())  #1700 lub 1500 nie licząc nadgodzin