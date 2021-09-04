from Ex_01_Wild_Cat.vehicle import Vehicle

class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION