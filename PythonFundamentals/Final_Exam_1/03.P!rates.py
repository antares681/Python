towns= {}
data = input()

while not data == 'Sail':
    town, population, gold = data.split('||')
    population, gold = int(population), int(gold)
    if not town in towns:
        towns[town] = [int(population), int(gold)]
    else:
        towns[town][0] += population
        towns[town][1] += gold
    data = input()

event = input()

while not event == 'End':
    event = event.split('=>')
    action = event[0]

    if action == 'Plunder':
        town, people, plunder = event[1:]
        people, plunder = int(people), int(plunder)
        towns[town][0] -= people
        towns[town][1] -= plunder
        print(f"{town} plundered! {plunder} gold stolen, {people} citizens killed.")
        if towns[town][0] <= 0 or towns[town][1] <= 0:
            print(f"{town} has been wiped off the map!")
            del towns[town]

    elif action == 'Prosper':
        town, income = event[1:]
        income = int(income)
        if income < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            towns[town][1] += income
            print(f'{income} gold added to the city treasury. {town} now has {towns[town][1]} gold.')
    event = input()

print(f'Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:')

towns = sorted(towns.items(), key=lambda x: (-x[1][1], x[0]))
for town, asset in towns:
    print(f'{town} -> Population: {asset[0]} citizens, Gold: {asset[1]} kg')
