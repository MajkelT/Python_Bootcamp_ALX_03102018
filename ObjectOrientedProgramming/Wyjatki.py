lista = [1, 2, 3, 4]

try:
    print(lista[5])
    list.add(5)
# except Exception as e:
#     print("Wystąpił jakiś błąd")
#     print(e)

except IndexError as e:
    #print("Próbujesz pobrać jakiś element spoza listy")
    raise IndexError ("Próbjesz pobrać jakiś element spoza listy")  #rzucanie wyjątku
    #rzucanie wyjątku - spowodowac przerwanie prog w sposób kontrolowany
except AttributeError as e:
    print("Prawdopodobnie wywołujesz metodę, której ten obiekt nie ma")

print("aAAA")