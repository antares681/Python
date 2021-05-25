class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, letter):
        product_to_print = [i for i in self.products if i[0] == letter]
        return product_to_print

    def __repr__(self):
        result = f'Items in the {self.name} catalogue:\n'
        sorted_product = sorted(self.products)
        result += '\n'.join(sorted_product)
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
