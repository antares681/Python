class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_pepperoni(cls):
        return cls(['peperronni', 'ham', 'mushrooms'])

print(Pizza.from_pepperoni())