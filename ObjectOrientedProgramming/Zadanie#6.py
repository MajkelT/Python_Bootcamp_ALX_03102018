class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Wektor {self.x}, {self.y}"

    def __add__(self, other):    #self to jest to co jest wywoływane #other to co dodawane
        nowy_x = self.x + other.x
        nowy_y = self.y + other.y
        return Vector(nowy_x, nowy_y)

    def __sub__(self, other):    #odejmowanie
        return (self.x - other.x, self.y - other.y)

    def __mul__(self, other):    #mnożenie
        if isinstance(other, Vector):     #sprawdzamy, czy other jest wektorem, czy other jest instacją wektora
            return self.x * other.x + self.y * other.y
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x*other, self.y*other)
        else:
            return Vector(self.x * len(other), self.y * len(other))

    def __lt__(self, other):
        d1 = (self.x ** 2 + self.y ** 2) ** (1 / 2)
        d2 = (other.x ** 2 + other.y **2) ** (1 / 2)
        return d1 < d2

    def __truediv__(self, other):
        if isinstance(other, Vector):     #sprawdzamy, czy other jest wektorem, czy other jest instacją wektora
            return self.x / other.x + self.y / other.y
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x / other, self.y / other)
        else:
            return Vector(self.x / len(other), self.y / len(other))
# w googlu opis dosępnych metod ==> python dunder methods

v1 = Vector (1,3)
v2 = Vector (2,2)
print(v1)
print(v2)

v3 = v1 + v2
print(v3)    #to samo co v4 = v1.__add__(v2)

print (v2 < v1)
v4 = v2 - v1
print(v4)  #odejmowaine wektorów

print(v1 * 5)
print(v1 * "Ala ma kota")

print(v1.__truediv__(v2))
print(v1 / v2)
print(v3 *(v1/v2))






# Kontakt Krzysztof: k.adamek@alx.pl
