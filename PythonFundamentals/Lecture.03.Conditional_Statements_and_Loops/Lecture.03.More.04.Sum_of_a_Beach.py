#VARIANT 1
sum_of_beach = input().lower()
element_counter = 0
lookup_list = ['sand', 'water', 'fish', 'sun']

for i in lookup_list:
    element_counter += sum_of_beach.count(i)

print(element_counter)

#VARIANT 2
# entry = input().lower()
# sun = entry.count('sun')
# water = entry.count('water')
# sand = entry.count('sand')
# fish = entry.count('fish')
# print(sun + water + fish + sand)