from Zadanie#1 import Product

class Basket():
    def __init__(self):

    def add_product(self, product, qty):
        pass

    def count_total_price(self):
        pass

    def generate_report(self):
        pass


basket = Basket()
product = Product(1, 'Woda', 10.00)
basket.add_product(product, 5)
print(basket.count_total_price())
print(basket.generate_report())
