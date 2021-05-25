data = input()
products = {}
name = ''
product_attributes = []

while not data == 'buy':
    name, price, quantity = data.split()

    if name not in products:
        product_attributes += float(price), int(quantity)
        products[name] = product_attributes
    else:
        products[name][0] = float(price)
        products[name][1] += int(quantity)
    product_attributes = []
    data = input()
for k, v in products.items():
    print(f'{k} -> {(v[0] * v[1]):.2f}')