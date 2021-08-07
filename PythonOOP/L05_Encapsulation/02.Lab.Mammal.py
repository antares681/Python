class Mammal:
    __kingdom = 'animals'
    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound


    def make_sound(self):
        return f'{self.name} makes {self.sound}'

    def get_kingdom(self):
        return Mammal.__kingdom   # can be called self.__kingdom, but good practice is to call it trough the class

    def info(self):
        return f'{self.name} is of type {self.type}'

mammal = Mammal("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())

