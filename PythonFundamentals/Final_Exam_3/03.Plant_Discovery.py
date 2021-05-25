def plant_gathering():
   plants_rarity_list = {}
   n = int(input())
   for _ in range(n):
        plant_data = input().split('<->')
        plants_rarity_list[plant_data[0]] = [int(plant_data[1]), []]
   return plants_rarity_list

def command_analyzer(command, plants_rarity_list):
    while not command == 'Exhibition':
        command = command.split(': ')
        instruction, data = command[0], command[1]

        if instruction == 'Rate':
            rater(data, plants_rarity_list)

        elif instruction == 'Update':
            updater(data, plants_rarity_list)

        elif instruction == 'Reset':
            reseter(data, plants_rarity_list)
        else:
            print('error')
        command = input()
    return plants_rarity_list

def rater(data, plants_rarity_list):
    plant, rating = data.split(' - ')
    if not plant in plants_rarity_list:
        print('error')
    else:
        plants_rarity_list[plant][1].append(int(rating))
    return plants_rarity_list

def updater(data, plants_rarity_list):
    plant, new_rarity = data.split(' - ')
    if not plant in plants_rarity_list:
        print('error')
    else:
        plants_rarity_list[plant][0] = int(new_rarity)

def reseter(data, plants_rarity_list):
    if not data in plants_rarity_list:
        print('error')
    else:
        plants_rarity_list[data][1].clear()
        return plants_rarity_list

def result_sorter(plants_rarity_list):
    for plant in plants_rarity_list:
        if plants_rarity_list[plant][1]:
            if not plants_rarity_list[plant][1] == 0:
                plants_rarity_list[plant][1] = sum(plants_rarity_list[plant][1]) / len(plants_rarity_list[plant][1])
        else:
            plants_rarity_list[plant][1] = 0
    return dict(sorted(plants_rarity_list.items(), key=lambda x: (-x[1][0], -x[1][1])))

def result_printer():
    print('Plants for the exhibition:')
    for plant, ratings in plants_sorted_list.items():
        print(f'- {plant}; Rarity: {ratings[0]}; Rating: {ratings[1]:.2f}')

plants_list = plant_gathering()
plants_sorted_list = result_sorter((command_analyzer(input(),plants_list)))
result_printer()
