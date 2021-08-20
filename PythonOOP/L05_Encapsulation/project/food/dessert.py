from Ex02_Movie_World.food.food import Food


class Dessert(Food):
    def __init__(self, name, price, grams, calories:float):
        self.__calories = calories
        super().__init__(name, price, grams)

    @property
    def calories(self):
        return self.__calories