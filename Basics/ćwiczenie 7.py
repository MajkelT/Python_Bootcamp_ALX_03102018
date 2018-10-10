liczba = int(input("Podaj liczbę: "))

print(f"Podzielna przez 2: {liczba%2 == 0}")
print(f"Podzielna prze 3 i większa od 10: {liczba%3==0 and liczba>10}")
print(f"Większa od 10 lub jest to liczba 7: {liczba>10 or liczba ==7}")


wynik = liczba == 7 or (
        liczba % 2 == 0 and
        liczba % 3 == 0 and
        liczba >10
)