class Child:
    days_in_month = 30
    def __init__(self, food_cost:int, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = list(toys_cost)
        self.cost:float = self.food_cost + sum(toys_cost)

    def get_monthly_expense(self):
        return self.cost * self.days_in_month
