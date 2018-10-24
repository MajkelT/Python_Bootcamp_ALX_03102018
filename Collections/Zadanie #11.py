a = {1,2,3,4}
b = {4,5,6,7}

print ("Suma", a | b)
print ("Różnica", a - b)
print ("Iloczyn, czyli część wspólna", a & b)
print ("Różnica symetryczna", a ^ b)
print("")

print(set(range(1,100,2)))  # liczy nieparzyste od 1 do 100
# samo range jest tylko obiektem, trzeba by po nim przejść pętlą for, żeby było widać liczby
# albo trzeba zrzutować na zbiór (set)

x = {49,81,50,20}
y = set(range(1,100,2))

print("Część wspólna x i y: ", x&y)


# zadanie 10
i = 0
zbior = set()
while True:
    liczba = input("wprowadź liczbę")
    if liczba == "k":
        break
    if type(liczba) != int:
        print("Możesz wprowadzać tylko liczby")
        continue
    zbior.add(int(liczba))
    i += 1
print(zbior)
