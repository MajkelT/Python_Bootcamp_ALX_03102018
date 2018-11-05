napis = "Ten $produkt kosztuje $cena"
napis2 = "Zajecia z $przedmiot zostaly odwolane"

slownik = {
    "produkt" : "Samochod",
    "cena" : "20000",
    "przedmiot" : "Fizyki",
    }

def formatuj(*napisy, **slownik ):
    wynik = []
    for napis in napisy:
        for klucz in slownik:
            print (klucz)
            napis = napis.replace("$"+klucz, slownik[klucz])
        wynik.append(napis)
        if len (wynik ) == 1:
            print(wynik[0])
            return wynik[0]

    return wynik

assert formatuj(napis, produkt="Samochod", cena="20000") == "Ten Samochod kosztuje 20000"
assert formatuj(napis2, przedmiot="Fizyki") == "Zajecia z Fizyki zostaly odwolane"
assert formatuj(napis, napis2, przedmiot="Fizyki") == "Zajecia z Fizyki zostaly odwolane"

