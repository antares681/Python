from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self, name:str, weight:float, food_eaten=0):
        return

class Bird(Animal):
    @abstractmethod
    def __init__(wing_size:float):
        pass

class Mammal(Animal):
    @abstractmethod
    def __init__(self, livng_region:str):
        self.livng_region = livng_region
        
        
