import re
regex = re.compile(r'([#\|])(?P<item_name>[A-Za-z\s]+)\1(?P<exp_date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)\1')
matches = dict()
calories = []
food_collection = []
data = input()
for match in regex.finditer(data):
    matches = match.groupdict()
    calories.append(int(matches['calories']))
    food_collection.append(matches)

days_to_last = sum(calories) //2000

print(f"You have food to last you for: {days_to_last} days!")
if food_collection:
    for _ in food_collection:
        print(f"Item: {_['item_name']}, Best before: {_['exp_date']}, Nutrition: {_['calories']}")