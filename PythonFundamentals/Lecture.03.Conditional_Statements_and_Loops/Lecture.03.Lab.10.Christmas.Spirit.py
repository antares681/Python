quantity = int(input())
day_left = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garlands_price = 3
tree_lights_price = 15
christmas_spirit_counter = 0
day_counter = 0
expenditure = 0

while not day_left == 0:
    day_counter += 1
    day_left -= 1
    if day_counter % 11 == 0:
        quantity += 2
    if day_counter % 2 == 0:
        expenditure += quantity * ornament_set_price
        christmas_spirit_counter += 5
    if day_counter % 3 == 0:
        expenditure += quantity * (tree_skirt_price + tree_garlands_price)
        christmas_spirit_counter += 13
    if day_counter % 5 == 0:
        expenditure += quantity * tree_lights_price
        christmas_spirit_counter += 17
    if day_counter % 3 == 0 and day_counter % 5 == 0:
        christmas_spirit_counter += 30
    if day_counter % 10 == 0:
        christmas_spirit_counter -= 20
        expenditure += tree_skirt_price + tree_garlands_price + tree_lights_price

if day_counter % 10 == 0:
    christmas_spirit_counter -= 30
print(f'Total cost: {expenditure}')
print(f'Total spirit: {christmas_spirit_counter}')

