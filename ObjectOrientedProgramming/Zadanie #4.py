class Product():

    def __init__(self, nazwa, id, cena):
        self.nazwa = nazwa
        self.ID = id
        self.cena = cena

    def print_info(self):
        print(f"Nazwa: {self.nazwa}, ID: {self.ID}, Cena:{self.cena}")

class Basket():
    def __init__(self):
        #nic nie podajemy, bo definiujemy dopiero przy dodawaniu produktu
        self.koszyk = {}

    def add_product(self, produkt, qty):
        self.produkt = produkt
        self.qty = qty

        if self.koszyk == {}:
            self.koszyk[produkt.nazwa] = qty

        elif not produkt.nazwa in self.koszyk:
            self.koszyk[produkt.nazwa] = qty

        else:
            for element in self.koszyk:
                if produkt.nazwa in self.koszyk:
                    #self.qty = self.koszyk[element] + qty
                    #self.qty = qty_temp + qty
                    self.koszyk[self.produkt.nazwa] = self.koszyk[element] + self.qty
                    self.qty = 0

        print(basket.koszyk)






#     def count_total_price(self):
#         pass
#
#     def generate_report(self):
#         pass

woda = Product("woda", 222, 10.99)
ziemniaki = Product("ziemniaki", 21, 1.00)
buraki = Product("buraki", 10, 2.00)
woda.print_info()
ziemniaki.print_info()
basket = Basket()
basket.add_product(ziemniaki, 1)
basket.add_product(ziemniaki, 2)
basket.add_product(ziemniaki, 3)
basket.add_product(woda, 4)
basket.add_product(woda, 5)
basket.add_product(woda, 6)
basket.add_product(buraki, 7)
basket.add_product(buraki, 8)
basket.add_product(buraki, 9)
# print(basket.koszyk)

# print(basket.count_total_price())
# print(basket.generate_report())


