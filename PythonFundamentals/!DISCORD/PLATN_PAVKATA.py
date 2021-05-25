our_dict ={}
for c in range(int(input())):
    key, rarity = input().split("<->")
    our_dict[key] = [int(rarity), []]

command = input()
while command != 'Exhibition':
    task, doing = command.split(': ')
    if task == 'Rate':
        p, r = doing.split(" - ")
        if p in our_dict:
            our_dict[p][1].append(int(r))
        else:
            print('error')
    elif task == 'Update':
        p, new_rarity = doing.split(" - ")
        if p in our_dict:
            our_dict[p][0] = int(new_rarity)
        else:
            print('error')
    elif task == 'Reset':
        p = doing
        if p in our_dict:
            our_dict[p][1].clear()
        else:
            print('error')

    command = input()
new = {}
print('Plants for the exhibition:')
for key, value in our_dict.items():
    if len(our_dict[key][1]) != 0:
        average = sum([c for c in our_dict[key][1]]) / len(our_dict[key][1])
    else:
        average = 0

    new[key] = [value[0], average]

for key, value in sorted(new.items(), key=lambda z: (-z[1][0], -z[1][1])):
    print(f'- {key}; Rarity: {value[0]}; Rating: {value[1]:.2f}')