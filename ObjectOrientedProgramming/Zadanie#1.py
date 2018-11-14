class Product():

    def __init__(self, nazwa, id, cena):
        self.dupa = nazwa
        self.ID = id
        self.cena = cena

    def print_info(self):
        print(f"Nazwa: {self.dupa}, ID: {self.ID}, Cena:{self.cena}")

produkt = Product("woda", 222, 10.99)
produkt.print_info()



