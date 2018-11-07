class Animal:
    krolestwo = "Fauna"  #atrybut klasowy

    def __init__(self, nazwa):  # od razu definiuję nazwę
        self.nazwa = nazwa # przypisuje do selfa nazwę --> self wskazuje na tą instancję
    pass

zyrafa = Animal()  # konstruowanie obiektu żyrafa - tu muszę użyć już dwóch nawiasów
mysz = Animal()  # to jest instancja klasy  (mysz to instancja, Animal to klasa)
print(type(zyrafa))  # zwróci: <class '__main__.Animal'>
print(zyrafa.krolestwo)  # zwróci: Fauna  --> tzw. instancja klasy
print(mysz.krolestwo)   # zwróci: Fauna  --> tzw. instancja klasy

#atrybut klasowy można zmodyfikować i poprzez instancję i poprzez klasę
Animal.krolestwo = "Flora"  # modyfikacja poorzez klasę
print(zyrafa.krolestwo)  # zwróci: Flora
print(mysz.krolestwo)   # zwróci: Flora

zyrafa.krolestwo = "Fauna"  # modyfikacja poprzez instancję
print(zyrafa.krolestwo)  # zwróci: Fauna
print(mysz.krolestwo)   # zwróci: Flora



from Wprowadzenie import Animal  #import z nazwy pliku
a = Animal()
print(type(a))

# To będzie zwrócone:
# <class '__main__.Animal'>
# <class 'Wprowadzenie.Animal'>
# <class 'Wprowadzenie.Animal'>
# <class 'Wprowadzenie.Animal'>