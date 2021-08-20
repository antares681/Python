from math import pi

class Shape:
    def get_area(self):
        return None

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def get_area(self):
        return 0.5 * self.a * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return pi*self.r**2

#TODO polimorphism!

shapes = [Triangle(3,6), Square(15), Square(3), Circle(7)]

for shape in shapes:
    print(shape.get_area())

