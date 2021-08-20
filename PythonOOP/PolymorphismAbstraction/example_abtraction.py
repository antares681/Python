class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'My name is {self.name}'

    def __len__(self):
        return len(self.name)

    def __add__(self, other):
        return self.age - other

p = Person('test', 20)
print(p)
print(len(p))
print(p + 5)

# EXAMPLE 2
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        # raise NotImplementedError('Not implemented')

    @abstractmethod   #TODO -> abstract class method is MANDATORY
    def perimeter(self):
        pass
        # raise Exception('This is an abstract class')

class Triangle(Shape):
    def __init__(self, side, h):
        self.side = side
        self.h = h

    def area(self):
        return self.side * 0.5 * self.h

    def perimeter(self):
        return 'perimeter'

t = Triangle(5,6)
print(t.area())


#TODO EXAMPLE 3

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        raise NotImplementedError('Subclass must be implemented!')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)