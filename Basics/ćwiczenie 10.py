a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
operacja = input("Podaj rodzaj operacji: +-*/")

if operacja == "+":
    wynik = a + b
elif operacja == "-":
    wynik = a-b
elif operacja == "*":
    wynik = a*b
elif operacja == "/":
    if b == 0:
        wynik = "Nie dziel przez zero"
    else:
        wynik = a/b
else:
    print("Niezrozumiała operacja")

print(f"Wynik działania {operacja} na argumentach: {a}, {b} to: {wynik}")