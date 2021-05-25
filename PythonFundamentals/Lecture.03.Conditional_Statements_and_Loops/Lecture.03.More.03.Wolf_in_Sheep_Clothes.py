herd_list = input().split(', ')
j = 1
endangered_sheep_index = 0

if herd_list[-1] == "wolf":
    print('Please go away and stop eating my sheep')
else:

    for i in range(len(herd_list) - 1):
        x = herd_list[len(herd_list) - j]
        j+=1

        if x == 'wolf':
            print(f'Oi! Sheep number {endangered_sheep_index}! You are about to be eaten by a wolf!')
            break
        endangered_sheep_index += 1
