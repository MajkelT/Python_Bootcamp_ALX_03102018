import json

obiekt = {"imie": "Jan", "wiek": 33}   #slownik
print(json.dumps(obiekt))  #napis

napis = '{"imie": "Jan", "wiek": 33}' #slownik
print(type(json.loads(napis)))  #slownik

print(json.loads(napis)["wiek"])  #zapytanie do slownika - zwroci wartosc dla key wiek = 33
#loadS = czyta napis i wczytuje jego strukture
#load = wczytuje jakis plik

#ZADANIE nr 1

try:
    with open("pracownicy.json", "r") as plik:
        pracownicy = json.load(plik)
except FileNotFoundError:
    pracownicy = []

op = input("Co chcesz zrobic? [d - dodaj, w - wypisz]: ")
if op == 'd':
    imie = input("Imie: ")
    nazwisko = input("Nazwisko: ")
    rok_ur = int(input("Rok urodzenia: "))
    pensja = float(input("Pensja: "))
    pracownicy.append({"imie": imie,
                      "nazwisko": nazwisko,
                      "rok urodzenia": rok_ur,
                      "pensja": pensja})
    with open("pracownicy.json", "w") as plik:     # CTRL + Q - podglad dokumentacji
        json.dump(pracownicy, plik)
elif op == 'w':
    for nr, p in enumerate(pracownicy, 1):    #zwraca pare liczb w postaci tupli np (1, 2), zaczyna lczyc od 1
        print(f"- [{nr}] {p['imie']} {p['nazwisko']} {p['rok urodzenia']} {p['pensja']} PLN")

