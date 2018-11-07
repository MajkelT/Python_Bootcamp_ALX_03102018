# wersja moja
def silnia(x):
    wynik = 1
    if x == 0 or x == 1:
        wynik = 1
    else:
        for x in range(1, x):
            wynik = wynik * (x+1)
    return wynik

# wersja z rekurencją
def silnia(y):
    if y == 0:
        return 1
    else:
        return y * silnia(y -1)

print(silnia(0))
print(silnia(1))
print(silnia(2))
print(silnia(3))
print(silnia(4))
print(silnia(5))


def test_silnia():
    assert silnia(0) == 1
    assert silnia(1) == 1
    assert silnia(5) == 120

