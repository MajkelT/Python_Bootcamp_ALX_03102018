import sys

try:
    print(sys.argv[0])    #zamieni nazwę pliku po python wraz z argumentami na listę i zwróci pierwszy element
except IndexError:
    print("Zapomniałeś podać nawę pliku")

print("Ścieżka do pliku to: ", sys.argv[1])

with open(sys.argv[1], "r", encoding='utf8') as f:
    i = 0
    for linia in enumerate(f):    #enumerate dopisuje cyfrę, a potem linia tekstu
        i += 1
        print(i, linia, end="")
