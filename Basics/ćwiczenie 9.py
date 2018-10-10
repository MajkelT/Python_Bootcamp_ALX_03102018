rokUrodzenia = int(input("Podaj rok urodzenia: "))
dzis = 2018
wiek = dzis - rokUrodzenia
if wiek > 18:
    print("Jesteś pełnoletni")
else:
    print("Jesteś niepełnoletni")