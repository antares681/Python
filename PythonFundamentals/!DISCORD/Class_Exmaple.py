class a:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def get_age(self):
        return self.age

    def get_old(self):
        increase = int(input())
        self.age += increase


az = a('pavel', 12)
print(az.get_age())
az.get_old()
print(az.get_age())

az2 = a('Lazar', 44)
print(az2.get_age())
az2.get_old()
print(az2.get_age())