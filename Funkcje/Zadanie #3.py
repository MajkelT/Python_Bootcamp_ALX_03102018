def policz_znaki(napis, start = "<", end=">"):
    ile_znakow = 0
    poziom = 0

    for znak in napis:

        if znak == start:
            poziom += 1
        elif znak == end:
            poziom -= 1
        else:
            ile_znakow += poziom

    return ile_znakow

    # for litera in napis:
    #     if litera == start:
    #         czy_liczyć = True
    #     elif litera == end:
    #         czy_liczyć = False
    #     elif czy_liczyć:
    #         ile_znakow += 1
    # return ile_znakow


def test_policz_znaki_bez_znacznkow():
    assert policz_znaki('ala ma kota a kot ma ale') == 0 #nie ma żadnego poziomu zagłębienia

def test_policz_znaki_jeden_poziom_zagłębienia_standardowe_znaczniki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test_policz_znaki_wiele_poziomów_zagłębienia_niestandardowe_znaczniki():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', start = '[', end = ']') == 18

def test_policz_znaki_standardowe_znaczniki_wiele_poziomów():
    assert policz_znaki('a <a<a<a>>>') == 6