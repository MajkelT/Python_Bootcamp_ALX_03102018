lista = [5, 3, 2, 4, 1]
       #[0, 1, 2, 3, 5]

print("Liczby przed: ", lista)

for indeks_podstawienia in range(len(lista)):
    indeks_min_wartosci = indeks_podstawienia
    for indeks_ogona in range(indeks_podstawienia+1, len(lista)):
        if lista[indeks_ogona] < lista[indeks_min_wartosci]:
            indeks_min_wartosci = indeks_ogona
        value_temp = lista[indeks_min_wartosci]
        lista[indeks_min_wartosci] = lista[indeks_podstawienia]
        lista[indeks_podstawienia] = value_temp

        #lista[indeks_min_wartosci], lista[indeks_podstawienia] = lista[indeks_podstawienia], lista[indeks_min_wartosci]
print("Liczby po: ", lista)
assert lista == [1,2,3,4,5]