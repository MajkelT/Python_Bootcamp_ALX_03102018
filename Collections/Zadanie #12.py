min_ = int(input("Podaj cyfrę z lewej strony zbioru: "))
max_ = int(input("Podaj cyfrę z prawej strony zbioru: "))
ile = int(input("Podaj ile elementów ma mieć zbiór: "))

tablica_unsorted = []
tablica_sorted = []

# losowanie zbioru liczb
from random import randint
i = 1
while i <= ile:
    tablica_unsorted.append(randint(min_, max_))
    i += 1

#przechodzenie przez kolejne lcizby w wylosowanej tablicy
print("Tablica nieposortowana: ", tablica_unsorted)
x = 0
while x <= ile:
    if tablica_unsorted == []:
        break
    #print("Tablica nieposortowana przed pobraniem min: ", tablica_unsorted)
    a = min(tablica_unsorted)
    tablica_sorted.append(tablica_unsorted.pop(tablica_unsorted.index(a)))
    #print("Tablica posortowana: ", tablica_sorted)

print("Tablica posortowana:   ", tablica_sorted)
