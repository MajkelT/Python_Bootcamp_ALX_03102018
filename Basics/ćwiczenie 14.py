i = 0
max = None
min = None

while True:
    liczba = (input("Podaj liczbę: "))
    if liczba == "koniec" :        # wprowadzneie "koniec" przerywa pętlę
        break

    if  max is None or i == 0:
        max = min = int(liczba)
    elif int(liczba) > max:   # dzięki temu bierzesz pod uwage liczby ujemne
        max = int(liczba)
    elif min is None or int(liczba) < min:
        min = int(liczba)
    else: max = min
    # else:
    #     max = min

    i = i + 1
if max is None:
    print("Nie wprowadzono danych")
else:
    print("Max liczba:", max)
    print("Min liczba:", min)


