def result_sorter(plants_rarity_list):
    for plant in plants_rarity_list:
        if plants_rarity_list[plant][1]:
            if not plants_rarity_list[plant][1] == 0:
                plants_rarity_list[plant][1] = sum(plants_rarity_list[plant][1]) / len(plants_rarity_list[plant][1])
        else:
            plants_rarity_list[plant][1] = 0
    return sorted(plants_rarity_list.items(), key=lambda x: (-x[1][0], -x[1][1]))

def result_printer(sorted_list):
    print('Plants for the exhibition:')
    for plant, ratings in sorted_list:
        print(f'- {plant}; Rarity: {ratings[0]}; Rating: {ratings[1]:.2f}')

plants_rarity_list = {}

command = input()
while not command == 'Exhibition':
    command = command.split(': ')
    instruction, data = command[0], command[1]

    if instruction == 'Rate':
        plant, rating = data.split(' - ')
        if not plant in plants_rarity_list:
            print('error')
        else:
            plants_rarity_list[plant][1].append(int(rating))

    elif instruction == 'Update':
        plant, new_rarity = data.split(' - ')
        if not plant in plants_rarity_list:
            print('error')
        else:
            plants_rarity_list[plant][0] = int(new_rarity)

    elif instruction == 'Reset':
        plant = data
        if not plant in plants_rarity_list:
            print('error')
        else:
            plants_rarity_list[plant][1].clear()
    else:
        print('error')
    command = input()

plants_sorted_list = result_sorter(plants_rarity_list)
result_printer(plants_sorted_list)

# for key, value in plants_rarity_list.items():
#     if len(plants_rarity_list[key][1]) != 0:
#         average = sum([c for c in plants_rarity_list[key][1]]) / len(plants_rarity_list[key][1])
#     else:
#         average = 0
#     plants_rarity_list[key] = [value[0], average]

# while not command == 'Exhibition':
#     command = command.split(': ')
#     instruction, data = command[0], command[1]
#     if instruction == 'Rate':
#         plants_rarity_list = rater(data, plants_rarity_list)
#     elif instruction == 'Update':
#         plants_rarity_list = updater(data, plants_rarity_list)
#     elif instruction == 'Reset':
#         plants_rarity_list = reseter(data, plants_rarity_list)
#     else:
#         print('error')
#     command = input()


