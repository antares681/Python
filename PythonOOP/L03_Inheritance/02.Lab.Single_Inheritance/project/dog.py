#TODO from L03_Inheritance.Ex02_Zoo.animal import Animal
from project.animal import Animal

class Dog(Animal):
    def bark(self):
        return 'barking...'


# d = Dog()
# print(d.eat())