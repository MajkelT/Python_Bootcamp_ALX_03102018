

#zaczynamy od testów:
def wiecej_niz(napis, prog):
    wynik = set()
    for litera in napis:
        if napis.count(litera)>prog:
            wynik.add(litera)
    return wynik


def test_wicej_niz_dla_pustego_napisu():
    assert wiecej_niz("",0) == set()

def test_wiecej_niz_dla_niepustego_napisu():
    assert wiecej_niz("aaa bb mc", 3) == set()
    assert wiecej_niz("aaa bb mc", 2) == {'a'}