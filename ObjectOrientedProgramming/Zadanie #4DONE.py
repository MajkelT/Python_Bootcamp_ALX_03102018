class Product():

    def __init__(self, nazwa, id, cena):
        self.nazwa = nazwa
        self.ID = id
        self.cena = cena

    def print_info(self):
        print(f"Nazwa: {self.nazwa}, ID: {self.ID}, Cena:{self.cena}")

class BasketEntry:
    def __init__(self, product, quantity):
        """
        :param product: instance of Product class
        :param quantity: quantity of product - integer
        """
        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity

    def __str__(self):
        return f'{self.product.nazwa} x {self.product.quantity}'

    def generate_report(self):
        pass

class Basket():
    def __init__(self):
        self.entries = []

    def add_product(self, product, qty):
        self.entries.append(BasketEntry(product, qty))

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()
        return total_price

    def generate_report(self):
        out = "Produkty w koszyku :\n"
        for entry in self.entries:
            out += f'- {entry.product.nazwa} ({entry.product.id}), cena: {entry.product.cena}



# woda = Product("woda", 222, 10.99)
# ziemniaki = Product("ziemniaki", 21, 1.00)
# buraki = Product("buraki", 10, 2.00)
# woda.print_info()
# ziemniaki.print_info()
# buraki.print_info()
# basket = Basket()
# basket.add_product(ziemniaki, 1)
# basket.add_product(ziemniaki, 2)
# basket.add_product(ziemniaki, 3)
# basket.add_product(woda, 4)
# basket.add_product(woda, 5)
# basket.add_product(woda, 6)
# basket.add_product(buraki, 7)
# basket.add_product(buraki, 8)
# basket.add_product(buraki, 9)

pr1 = Product(1, "Woda", 2)
pr2 = Product(2, "Piwo", 3)
pr3 = Product(3, "Salceson", 5)
basket = Basket()
basket.add_product(pr1, 4)
basket.add_product(pr2, 2)
basket.add_product(pr3, 1)
basket.add_product(pr1, 3)

for e in basket.entries:
    print(e)



#assert basket.count_total_price == 8


class Product():
    ID = 1

    def __init__(self, nazwa, cena):
        self.id = Product.ID
        self.nazwa = nazwa
        self.cena = cena
        Product.ID += 1

    def print_info(self):
        print(f"Produkt {self.nazwa}, id: {self.id}, cena: {self.cena} PLN")

    def dej_cene(self):
        return self.cena


class BasketEntry:
    def __init__(self, product, quantity):
        """
        :param product: instance of Product class
        :param quantity: quantity of product - int
        """

        self.product = product
        self.quantity = quantity

    def count_price(self):
        return self.product.cena * self.quantity

    def __str__(self):
        return f'{self.product.nazwa} x {self.quantity}'

    def generate_report(self):
        return f'- {self.product.nazwa} ({self.product.id}), cena: {self.product.cena} x {self.quantity}\n'


class Basket:
    def __init__(self):
        self.entries = []

    def add_product(self, product, qty):
        self.entries.append(BasketEntry(product, qty))

    def count_total_price(self):
        total_price = 0
        for entry in self.entries:
            total_price += entry.count_price()
        return total_price

    def generate_report(self):
        out = "Produkty w koszyku:\n"
        for entry in self.entries:
            out += entry.generate_report()
        out += f"W sumie: {self.count_total_price()}"
        return out


pr1 = Product("Woda", 2)
pr2 = Product("Piwo", 3)
pr3 = Product("Salceson", 5)
basket = Basket()
basket.add_product(pr1, 4)
basket.add_product(pr2, 2)
basket.add_product(pr3, 1)
basket.add_product(pr1, 3)

print(basket.count_total_price())
print(basket.generate_report())
# assert basket.count_total_price() == 8