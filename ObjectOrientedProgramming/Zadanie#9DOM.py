#Zadanie #4 - klasa Basetk

class Product():
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa

        self.cena = cena
    def print_info(self):
        print(f"Nazwa: {self.nazwa}, Cena:{self.cena}")


class Basket:
    def __init__(self):
        self.koszyk = {}


    def add_product(self, nazwa, liczba):
        self.koszyk[nazwa] = liczba
        # for elements in koszyk:
        #     print(elements, "-", koszyk[elements])
        print(dict.items(self.koszyk))
        return

    def cout_total_price(self):
        pass

    def generate_report(self):
        pass

    # def __str__(self):
    #     return(self.koszyk)


winogrona = Product("winogorna", 20)
jablka = Product("jablka", 3)

koszyk = Basket()
koszyk.add_product(winogrona, 10)
koszyk.add_product(jablka, 5)
#print(koszyk)
