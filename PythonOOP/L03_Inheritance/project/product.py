class Product:
    def __init__(self, name:str, quantity:int):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity:int):
        self.quantity -= quantity

    def increase(self, quantity):
        self.quantity += quantity
