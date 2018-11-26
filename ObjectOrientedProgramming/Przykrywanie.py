class Square():
    def __init__(self, a):
        self.a = a
        self.field = self.a **2

    def __add__(self, other):
        print(isinstance(other, Square))
        return self.field + other.field

    def add_fields(self, other):
        return self.field + other.field


kw1 = Square(2)
kw2 = Square(3)

print(kw1.field)
print(kw2.field)

print(dir(kw1))
'''
['__add__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', '__weakref__', 'a', 'add_fields', 'field']
'''

# + ==> __add__
# - ==> __sub__
# * ==> __mul__
# / ==> _diw__

assert kw1 + kw2 == 13
assert kw1.__add__(kw2) == 13

print(isinstance(kw1, Square))