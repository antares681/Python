from abc import ABC, abstractmethod
from math import pi

import radius as radius


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius **2 * pi

    def calculate_perimeter(self):
        return self.radius * pi


class Rectangle(Shape):
    def __init__(self, h, w):
        self.h = h
        self.w = w

    def calculate_area(self):
        return self.h * self.w

    def calculate_perimeter(self):
        return (self.h + self.w) * 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())