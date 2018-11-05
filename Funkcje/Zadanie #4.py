# ARGS I KWARGS
def foo(pierwszy, *reszta):
    print (f"pierwszy: {pierwszy}")
    print (f"reszta: {reszta}")
    print(f"ostatni element: {reszta[-1]}") # ostatni element
    return pierwszy + reszta[-1]  # zwraca pierwszy i ostatni z *reszta

print(foo(1,2))
print(foo(1,2,5,10,15))

print("")

def druga_funkcja(**slownik):
    if 'd' in slownik:
        return slownik['a'] + slownik['d']
    return slownik ['a']

print('a', druga_funkcja(a=2))
print('a i d', druga_funkcja(a=2, b=2, c=3, d=4))
print('a i d drugi raz', druga_funkcja(a=2, b=2, c=3, d=14, zosia=5, adas=15))
print('a drugi raz ale bez d', druga_funkcja(a=2, b=2, c=3, d=14, zosia=5, adas=15))

print("")

co_na_co = {
    "Ala" : "Kot",
    "Kota" : "Alę"
}

#"Ala ma kota" --> "Kot ma Alę"

def zamien(jakis_tekst, **co_na_co):
    for klucz in co_na_co:
        jakis_tekst = jakis_tekst.replace(klucz, co_na_co[klucz])
    return jakis_tekst

print(zamien("Ala ma kota", ma="bije"))