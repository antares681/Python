from Ex02_Movie_World.beverage.hot_beverage import HotBeverage

class Tea(HotBeverage):
    def __init__(self, name, price, milliliters):
        super().__init__(name, price, milliliters)