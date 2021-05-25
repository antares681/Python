bread_products = input().split()
products = {}
print(bread_products)

for index in range(0, len(bread_products), 2):
    current_product = bread_products[index]   #SEPARATE VALUES
    quantity = int(bread_products[index + 1]) #SEPARATED KEYs
    products[current_product] = quantity      #ALLOCATE KEY TO VALUES IN DICT

print(products)

