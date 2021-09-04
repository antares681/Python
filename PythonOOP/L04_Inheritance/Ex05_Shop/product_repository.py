# from Ex05_Shop.food import Food
# from Ex05_Shop.drink import Drink

class ProductRepository():
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):
        that_product = [object for object in self.products if object.name == product_name]
        return that_product


    def remove(self, product_name: str):
        that_product = [object for object in self.products if object.name == product_name]
        if that_product:
            self.products.remove(that_product[0])

    def __repr__(self):
        return '\n'.join([f'{product.name}: {product.quantity}' for product in self.products])

# apple = Food('apple')
# d1 = Drink('Cola')
# d2 = Drink('Water')
# p_r = ProductRepository()
# p_r.add(apple)
# p_r.add(d1)
# p_r.add(d2)
# p_r.find('cola')
# a=5
# print(p_r)


