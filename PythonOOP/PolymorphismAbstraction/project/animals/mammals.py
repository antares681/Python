from abc import ABC, abstractmethod
from project.animals.animal import Animal

@abstractmethod
class Mammal(ABC):
    def super().__init__(self):


class Mouse(Mammal):
    def make_sound(self):
        return 'Squeak'

class Dog(Mammal):
    def make_sound(self):
        return 'Woof!'

class Cat(Mammal):
    def make_sound(self):
        return 'Meaow'

class Tiger(Mammal):
    def make_sound(self):
        return 'ROAR!!!'