MiastoA = input("Wpisz nazwę miejscowości A: ")
MiastoB = input("wpisz nazwę miejscowośći B: ")
Dystans = int(input(f"Dystans {MiastoA}-{MiastoB}: "))
            #DystansAB = float(input("Podaj dystans pomiędzy miastami A i B: "))
CenaPaliwa = float(input("Podaj cenę paliwa za 1 litr: "))
Spalanie = float(input ("Podaj spalanie na 100 km: "))
Koszt = round(CenaPaliwa*Spalanie*Dystans, 2)

print("Koszt przejazdu:",Koszt)