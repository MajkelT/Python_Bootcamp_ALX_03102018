class Temperatura:
    def __init__(self, x):
        self.wartosc = x

    def __str__(self):
        return f"Temperatura: {self._wartosc} stopni Celcjusza."

    @property
    def wartosc(self):
        print("getter")
        return 2* self._wartosc

    @wartosc.setter
    def wartosc(self, x):
        print("setter")
        if x < -273:
            raise ValueError("Temperatura za niska")
        self._wartosc = x

x = Temperatura(20)   #setter
x.wartosc = 100       #setter
print(x)
print(x.wartosc)
x.wartosc = -200      #getter