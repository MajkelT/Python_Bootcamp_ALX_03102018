class ElectricCar():
    def __init__(self,max_range):
        self.range = max_range
        self.max_range = max_range

    def drive(self, distance):     #metoda drive
        if distance > self.range:
            wynik = self.range
            self.ragne = 0
            return wynik
        else:
            self.range -= distance
            return distance

        # self.range -= distance
        # if self.range <= 0:
        #     return print(f" {self.range} --> you need to refill!")
        # else:
        #     return (print(self.range))

    def charge(self):    #metoda charge
        self.range = self.max_range

car = ElectricCar(100)
print(car.drive(70))  # zwróci 30
print(car.drive(50))  # zwróci 30 - nie można przejechać więcej
car.charge()  # naładuje do 100
print(car.drive(50)) # zwróci 50