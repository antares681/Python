import re
regex = re.compile(r'(?<=(/))[A-Z][A-Za-z]{2,}(?=(/))|(?<=(=))[A-Z][A-Za-z]{2,}(?=(=))')
travel_points = 0
destinations = []
data = input()

for match in regex.finditer(data):
    destinations.append(match.group())
    travel_points += len(match.group())

print(f"Destinations: {', '.join(destinations)}")
print(f'Travel Points: {travel_points}')