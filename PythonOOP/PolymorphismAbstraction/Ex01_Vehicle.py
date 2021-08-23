from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self, value):
        return

    @abstractmethod
    def refuel(self, value):
        return

class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, km):
        self.fuel_consumption += 0.9
        if self.fuel_quantity >= self.fuel_consumption * km:
            self.fuel_quantity -= self.fuel_consumption * km
        return self.fuel_quantity

    def refuel(self, extra_fuel):
        self.fuel_quantity += extra_fuel
        return self.fuel_quantity


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, km):
        self.fuel_consumption += 1.6
        if self.fuel_quantity >= self.fuel_consumption * km:
            self.fuel_quantity -= self.fuel_consumption * km
        return self.fuel_quantity

    def refuel(self, extra_fuel):
        self.fuel_quantity += extra_fuel * 0.95
        return self.fuel_quantity

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
