def get_inventory_cost(name, inventory):
    return sum([get_item_cost(name, item) for item in inventory])

def get_item_cost(name, item):
    return item_cost[name][item]


data = input().split(', ')

heroes_inventories = {name: set() for name in data}
item_cost = {name: {} for name in data}

command = input()
while not command == 'End':
    name, item, cost = command.split('-')
    cost = int(cost)
    heroes_inventories[name].add(item)
    if item not in item_cost[name]:
        item_cost[name][item] = cost
    command = input()

##TODO unComment to see how it works
# print(heroes_inventories.items())
# print(item_cost)

[print(f'{name} -> Items: {len(inventory)}, Cost: {get_inventory_cost(name, inventory)}') for name, inventory in heroes_inventories.items()]
