from abc import ABC, abstractmethod
from math import pi

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
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2* pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width + self.height) * 2



# test circle
import unittest

class ShapesTests(unittest.TestCase):
    def test(self):
        c = Circle(5)
        self.assertEqual(c.calculate_area(), 78.53981633974483)
        self.assertEqual(c.calculate_perimeter(), 31.41592653589793)

if __name__ == "__main__":
    unittest.main()