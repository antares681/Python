#Abstractions
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

#Encapsulations
    @name.setter
    def name(self, value):
        if len(value) < 3:
            raise ValueError("Name must be at least 3 chars")
        self.__name = value

    @abstractmethod
    def sound(self):
        pass

#Inheritance
class Cat(Animal):
    def sound(self):
        return "Meow"


class Dog(Animal):
    def sound(self):
        return "Bau"

for animal in Cat('Sharo'), Dog('Oras'):
    print(animal.sound())

