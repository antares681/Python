class Circle():
    __pi = 3.14

    def __init__(self, diameter):
       self.diameter = diameter
       self.radius = diameter/2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * self.radius**2

    def calculate_area_of_sector(self, angle):
        return Circle.__pi * self.radius**2 * (angle/360)

#AUTO INPUTS

diameter = Circle(10)
angle = 5

print(f"{diameter.calculate_circumference():.2f}")
print(f"{diameter.calculate_area():.2f}")
print(f"{diameter.calculate_area_of_sector(angle):.2f}")