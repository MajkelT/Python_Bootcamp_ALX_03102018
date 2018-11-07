lista = [1, 2, 3, 4, 5, 6]

# warunek jest taki,m że większe niż 3
out = [False, False, False, True, True, True]

def bigger_than_3(liczba):
    if liczba > 3:
        return True
    return False

def smaller_than_3(liczba):
    if liczba < 3:
        return True
    return False

def sprawdzam_czy_wieksze_niż_3(lista):
    out = []
    for element in lista:
        out.append(bigger_than_3(element))  # to to samo co niżej wykomentowane
    #     if element > 3:
    #         out.append(True)
    #     else:
    #         out.append(False)

    return out

def sprawdzam_czy(lista,warunek):   #otrzymam listę na podstawie jakiegoś warunku,
                                    #inaczej jednym z argumentów jest inna funkcja
    """
    :param lista: lista wejściowa
    :param warunek: jakiś przepis, funkcja - jaki jest ten warunek
    :return:
    """
    for element in lista:
        out.append(bigger_than_3(element))
        if element > 3:
            out.append(True)
        else:
            out.append(False)


assert sprawdzam_czy_wieksze_niż_3(lista) == out

x = lambda i: i == 4 # --> takie proste zdefiniowanie funkcji wewnątrz kodu
print(type(x)) # --> zwróci funkcję
# poniżej jest napisana inna definicja tej funkcji:
def x(i)
    if i == 4:
        return True
    return False

assert sprawdzam_czy(lista, warunek = lambda x: x == 4) == [False, False, False, True, False, False]
# można to też tak zapisać:
assert sprawdzam_czy(lista, lambda x: x == 4) == [False, False, False, True, False, False]