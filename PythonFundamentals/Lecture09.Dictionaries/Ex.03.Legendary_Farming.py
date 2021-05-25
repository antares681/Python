junk = {}
key_materials = {'shards':0, 'fragments':0, 'motes':0 }
rewards = {'shards': 'Shadowmourne', 'fragments':'Valanyr', 'motes':'Dragonwrath' }
is_winner = False
data = input()

while is_winner is False:
    data = (data.lower()).split()
    for i in range(0, len(data),2):
        if data[i+1] not in key_materials:
            if data[i+1] not in junk:
                junk[data[i+1]] = int(data[i])
            else:
                junk[data[i+1]] += int(data[i])
        else:
            key_materials[data[i + 1]] += int(data[i])

        if key_materials['shards'] >= 250:
            is_winner = True
            gathered_material = 'shards'
            break
        elif key_materials["fragments"] >= 250:
            is_winner = True
            gathered_material = 'fragments'
            break
        elif key_materials["motes"] >= 250:
            gathered_material = 'motes'
            is_winner = True
            break
    if is_winner:
        break
    data = input()

#PRINT REWARD
print(f'{rewards[gathered_material]} obtained!')

#PRINT KEY MATERIALS
key_materials[gathered_material] -= 250
sorted_list = sorted(key_materials.items(), key = lambda x: (-x[1], x[0]), reverse = False)
for k,v in sorted_list:
    print(f'{k}: {v}')

#PRINT JUNK
junk_sorted = sorted(junk.items(), key = lambda x: x[0])
for k,v in junk_sorted:
    print(f'{k}: {v}')





# junk = {}
# key_materials = {'fragments': 0, 'motes':0 , 'shards':0}
# win = {'fragments': 'Valanyr',
#        'motes':'Dragonwrath',
#        'shards':'Shadowmourne'
# }
# command = input()
# o = {}
# is_break = False
# while command:
#     row = command.split()
#     for c in range(0, len(row), 2):
#         value = int(row[c])
#         key = row[c+1].lower()
#         if key in key_materials:
#             key_materials[key] += value
#             for i, f in key_materials.items(): # (key , value)
#                 if key_materials[i] >= 250:
#                     reward = win[i]
#                     print(f'{reward} obtained!')
#                     key_materials[i] -= 250
#                     is_break = True
#                     break
#         else:
#             if key in junk:
#                 junk[key] += value
#             else:
#                 junk[key] = value
#         if is_break:
#             break
#
#     if is_break:
#         break
#
#     command = input()
# for key, value in sorted(key_materials.items(), key=lambda x:(-x[1], x[0])):
#     print(f'{key}: {value}')
# for key , value in sorted(junk.items(), key=lambda x:x[0]):
#     print( f'{key}: {value}')