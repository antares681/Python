# data = input()
# products = {}
#
# while data == 'statistics':
#     product, quantity = data.split(': ')
#     quantity = int(quantity)
#     products[product] = quantity
#     data = input()
#     if product not in products:
#         products[product] = quantity
#     else:
#         products[product] += quantity
#
# print('Products in stock:')
#
# for product, quantity in products.items():
#     print(f"-{product}: {quantity}")
#
# print(f'Total Products: {len(products)}')
# print(f'')

kvp = []
kvp_dict = {}

data = input()
while not data == 'statistics':
   data = data.split(": ")
   kvp += data
   data = input()

for el in range(0, len(kvp), 2):
    key, val = kvp[el], int(kvp[el+1])

    if key in kvp_dict:
        kvp_dict[key] += val
    else:
        kvp_dict[key] = val

print(f'Products in stock:')
for k,v in kvp_dict.items():
    print(f"- {k}: {v}")

print(f'Total Product {len(kvp_dict)}')
print(f'Total Quantity {sum(kvp_dict.values())}')


