#tworzenie dekoratora bold (zadanie #8):
def bold(func):
    def wrapper(*args, **kwargs):      #funckja, która może przyjąć cokolwiek
        wynik = func(*args, **kwargs)
        return "<b>" + wynik + "<\\b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):      #funckja, która może przyjąć cokolwiek
        wynik = func(*args, **kwargs)
        return "<i>" + wynik + "<\\i>"
    return wrapper

@bold   #oznacza to samo co: nasza_funkcja = bold(italic(nasza_funkcja))
@italic
def nasza_funkcja():
    return "jakiś napis"

print(nasza_funkcja())
