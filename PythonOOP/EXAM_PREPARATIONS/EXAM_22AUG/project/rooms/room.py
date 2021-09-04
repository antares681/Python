class Room:
    def __init__(self, family_name, budget:float, members_count:int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children: list
        self.expenses = None


    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self.__expenses = value


    def calculate_expenses(self, *args):
        for items in args:
            self.expenses += sum(x.get_monthly_expense() for x in items)