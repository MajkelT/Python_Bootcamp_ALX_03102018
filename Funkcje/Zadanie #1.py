# def dodaj(a,b):
#     return a+b
#
# def test_dodaj_dwie_liczby():
#     assert dodaj(1, 2) == 3

def czy_pierwsza(cyferka):
    if cyferka == 1:
        return(True)

    for i in range(2, cyferka-1):
        if cyferka%i == 0:
            return False
    return True


#testy poprawności:
def test_czy_pierwsza_dla_liczby_pierwszej():
    assert czy_pierwsza(11)
    assert czy_pierwsza(3)
    assert czy_pierwsza(101)

def test_czy_pierwsza_dla_liczby_nie_pierwszej():
    assert not czy_pierwsza(27)
    assert not czy_pierwsza(4)
    assert not czy_pierwsza(8)