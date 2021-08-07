from vehicle import Vehicle

DEFAULT_FUEL_CONSUMPTION = 3

class Car(Vehicle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
