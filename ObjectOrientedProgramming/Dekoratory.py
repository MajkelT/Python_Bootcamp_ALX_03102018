def fun():
    print("Cześć")

#fun()
#funkcje są obiektami, wiec możemy je przekazywać jako argumenty

def prosty_dekorator(func):
    def wrapper(*args, **kwargs):     #args to proste rzeczy, kwargs to słowniki; tu definiujemy dowolną ilość argumentów
        print("Przed wywołaniem")
        result = func(*args, **kwargs)    #tu wypakowujemy te argumenty
        print("Po wywołaniu")
        return result
    return wrapper

def dwa_wywolaina(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper

@prosty_dekorator       #wywołuje funkcję fun() a potem pisze "cześć"
def fun():
    print("Cześć")

@prosty_dekorator    #pojawia się prosty dekorator a po nim funkcja silnia
def silnia(x):
    wynik = 1
    for i in range(1, x + 1):
        wynik *= i
    return wynik

#fun = prosty_dekorator(fun)  ==> dekorator zastępuje to i jest to tzw lukier syntaktyczny

print("Akuku")
fun()
print(silnia(5))


