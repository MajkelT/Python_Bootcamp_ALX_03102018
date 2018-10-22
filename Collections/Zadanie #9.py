produkty = {
    'kura': 10,
    'ziemniaki': 2,
    'szynka': 5,
    'piwo': 1.5}

for produkt in produkty:
    print(f" - {produkt} - w cenie: {produkty[produkt]} PLN")

wybor_produktu = input("Który produkt chcesz kupić? ")
ile = input(f"Ile chcesz kupić [{wybor_produktu}? ]")
do_zaplaty = int(ile)*produkty[wybor_produktu]
print("Zapłacisz: ", do_zaplaty, "PLN")



