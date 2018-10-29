def policz_znaki(napis, start, end)
for litera in napis:
    if litera == start:
        liczba_poziomow = litera.count()


    elif litera == end:
        liczenie = False

    litera.index("znak1")-litera.index("znak2")


def test_policz_znaki_bez_znacznkow()
    assert policz_znaki('ala ma <kota> a kot ma ale') == 0 #nie ma żadnego poziomu zagłębienia

def test_policz_znaki_jeden_poziom_zagłębienia_standardowe_znaczniki():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4

def test_policz_znaki_wiele_poziomów zagłębienia_niestandardowe_znaczniki():
    assert policz_znaki('ala [kota [a kot]] ma [ale]', start = '[', end = ']') == 18

def test_policz_znaki_standardowe_znaczniki_wiele_poziomów:
    assert policz_znaki('a <a<a<a>>>') == 6