produkty = {
    'kura': 10,
    'ziemniaki': 2,
    'szynka': 5,
    'piwo': 1.5}

magazyn = {
    'kura': 1,
    'ziemniaki': 3,
    'szynka': 2,
    'piwo': 1}

for produkt in produkty:
    print(f" - {produkt} - w cenie: {produkty[produkt]} PLN,\t liczba sztuk: {magazyn[produkt]}")

do_zaplaty = 0 #koszyk będzie w postaci słownika w drugiej wersji programu

print()
while True:
    i = 0
    komenda = input("""Wybierz opcję:
    [d] - dodaj do magazynu
    [k] - kup
    [z] - zakończ """)

    if komenda == "z":
        break

    if komenda == "d":
        dodanieProduktu = input("Podaj nazwę produktu: ")
        ile = input("Ile chcesz dodać nowego produktu? ")
        cena = input(f"jaka jest cena dodawanego produktu? ")
        produkty[dodanieProduktu] = int(cena)
        magazyn[dodanieProduktu] = int(ile)
        for produkt in produkty:
            print(f" - {produkt} - w cenie: {produkty[produkt]} PLN,\t liczba sztuk: {magazyn[produkt]}")

    if komenda == "k":
        wybor_produktu = input("Który produkt chcesz kupić? ")
        if not wybor_produktu in produkty:
            print("Sorry nie ma tego w sklepie")
            continue
        #wybor_produktu = input("Który produkt chcesz kupić? ")
        ile = input(f"Ile chcesz kupić [{wybor_produktu}? ]")
        if magazyn[wybor_produktu] < int(ile):
            print("Nie ma tyle produktu w magazynie")
            continue
        magazyn[wybor_produktu] -= int(ile)  #magazyn[wybor_produktu] = magazyn[wybor_produktu] - int(ile)
        for produkt in produkty:
            print(f" - {produkt} - w cenie: {produkty[produkt]} PLN,\t liczba sztuk: {magazyn[produkt]}")

        do_zaplaty = do_zaplaty + int(ile)*produkty[wybor_produktu]
    i += 1

print("Zapłacisz: ", do_zaplaty, "PLN")



