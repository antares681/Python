count_of_orders = int(input())
price_per_capsule = 0
total_price = 0
for order in range(count_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsule_count = int(input())
    price_per_month = (days * capsule_count) * price_per_capsule
    print(f'The price for the coffee is: ${price_per_month:.2f}')
    total_price += price_per_month

print(f'Total: ${total_price:.2f}')