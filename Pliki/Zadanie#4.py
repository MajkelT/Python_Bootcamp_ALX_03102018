import sys
import os

def tree(katalog, ile_wciec = 0):
    zawartosc = list(os.scandir(katalog))
    for elem in os.scandir(katalog):
        #print(f"{ile_wciec * '-'}{elem.name}")
        if elem.name == zawartosc [-1]:
            print(ile_wciec * '˪   ', elem.name, sep="")
        else:
            print(ile_wciec * '|   ', elem.name, sep = "")  #to to samo co wyzej
        if elem.is_dir():
            tree(elem, ile_wciec + 1)



directory = sys.argv[1]
tree(directory)
