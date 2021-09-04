from Ex05_Shop import Food

#TODO FOR SUBMISSIO USE:
# from L03_Inheritance.Ex02_Zoo.food import Food


class Fruit(Food):
   def __init__(self,name:str, expiration_date:str):
       super().__init__(expiration_date)
       self.name = name


#TODO TEST
# f = Fruit('banana', '2020-02-10')
# print(f.expiration_date)