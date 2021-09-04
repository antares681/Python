from Ex_01_Wild_Cat.car import Car, DEFAULT_FUEL_CONSUMPTION


class FamilyCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 3
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = DEFAULT_FUEL_CONSUMPTION