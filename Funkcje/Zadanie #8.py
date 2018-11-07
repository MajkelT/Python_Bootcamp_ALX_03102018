# DEKORATORY - funkcje, które zwracają inne funkcje
# w tym wypadku @bold dekoruje wynik o 'bold'
def bold(func):
    def wrapper(arg):
        return'<b>' + func(arg) + '</b>'

    return wrapper

@bold
def foo(arg):
    return f'Test {arg}'

print (foo(1))