def fun():
    print("Cześć")

class Klasa:
    def __call__(self, *args, **kwargs):
        print("No elo")

fun()
x = Klasa()
x()  #--> to zwraca funcję
