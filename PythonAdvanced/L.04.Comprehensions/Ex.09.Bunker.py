def get_category_items(category, bunker):
    return ', '.join([x for x in bunker[category]])

categories = input().split(', ')
bunker = {category: {} for category in categories}

lines = int(input())

for line in range(lines):
     category, food_name, food_properties = input().split(' - ')
     food_properties = {pair.split(':')[0]:int(pair.split(':')[1])
                        for pair in food_properties.split(';')}
     bunker[category][food_name] = food_properties


count_of_items = sum([item['quantity']
 for items_by_category
 in bunker.values()  # [{'pizza': {quality, quantity}}]
 for item           # {'quality':10, 'quantity': 5}
 in items_by_category.values()
 ])

avg_quality = sum([item['quality']
 for items_by_category
 in bunker.values()  # [{'pizza': {quality, quantity}}]
 for item           # {'quality':10, 'quantity': 5}
 in items_by_category.values()
 ]) / len(categories)

print(f'Count of items: {count_of_items}')
print(f'Average quality: {avg_quality:.2f}')

[print(f'{category} -> {get_category_items(category, bunker)}') for category in bunker.keys()]