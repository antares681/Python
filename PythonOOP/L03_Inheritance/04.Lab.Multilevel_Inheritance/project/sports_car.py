from project.car import Car
# from L03_Inheritance.Ex02_Zoo.car import Car

class SportsCar(Car):
    def race(self):
        return "racing..."

#TODO testing
# a = SportsCar()
# print(f'SportsCar is a Vehicle that is {a.move()} so it is a Car that is {a.drive()} and if this car is {a.race()} so it is a sports Car!')