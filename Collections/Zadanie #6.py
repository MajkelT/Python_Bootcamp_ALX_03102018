liczby = [5, 2, 1, 4, 3]

min_ = liczby[0]
max_ = liczby[0]

print(liczby)

for liczba in liczby:
    if liczba < min_:
        min_ = liczba
    if liczba > max_:
        max_ = liczba
print("Wartości min i max: ", min_, max_)
print(liczby.index(min_), liczby.index(max_))

liczby[liczby.index(min_)], liczby[liczby.index(max_)] = max_, min_  #na pozycję min wtawia obecny max i odwrotnie
# takie tuple to jest a,b = b,a

print(liczby)





