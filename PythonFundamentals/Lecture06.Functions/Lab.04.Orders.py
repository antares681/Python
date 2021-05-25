total_price = 0

coffee_price = 1.50
water_price = 1.00
coke_price = 1.40
snacks_price = 2.00

def price_calculator (product_type, product_quantity):
    result = None
    if product_type == 'coffee':
        result = coffee_price * product_quantity
    elif product_type == 'water':
        result = water_price * product_quantity
    elif product_type == 'coke':
        result = coke_price * product_quantity
    elif product_type == 'snacks':
        result = snacks_price * product_quantity
    return result

product = input()
quantity = int(input())

total_price = price_calculator(product, quantity)
print(f'{total_price:.2f}')