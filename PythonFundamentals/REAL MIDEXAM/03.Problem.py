price_ratings = [int(price) for price in input().split() if int(price) in range(-2*31, 2**31+1)]

entry_point = int(input())
command = input()

damage_left = []
damage_right =[]

right = [price_ratings[element] for element in range(entry_point + 1, len(price_ratings))]
left = [price_ratings[element] for element in range(entry_point)]

if command == "cheap":
    for element in range(len(right)):
        if right[element] < price_ratings[entry_point]:
            damage_right.append(right[element])

    for element in range(len(left)):
        if element < price_ratings[entry_point]:
            damage_left.append(left[element])

if command == "expensive":
    for element in range(len(right)):
        if right[element] >= price_ratings[entry_point]:
            damage_right.append(right[element])

    for element in range(len(left)):
        if left[element] >= price_ratings[entry_point]:
            damage_left.append(left[element])

damage_left = sum(damage_left)
damage_right = sum(damage_right)

if damage_right > damage_left:
    print(f'Right - {damage_right}')
else:
    print(f'Left - {damage_left}')

#TEST1 -2147483655 2 2 32 543 2147483655
#TEST2 -2 2 1 5 9 3 2 -2 1 -1 -3 3
#      7
#      expensive
#TEST3 1 5 1
#      1
#      cheap


ratings = list(map(int,input().split(" ")))
entry_point = int(input())
type_item = input() #ratings[entry_point] = 5
left = 0
right = 0
for i in range(entry_point-1,-1,-1): #Left
    if type_item == 'cheap':
       if ratings[i] < ratings[entry_point]:
           left += ratings[i]
    else:
        if ratings[i] >= ratings[entry_point]:
            left += ratings[i]

for i in range(entry_point+1,len(ratings)): #Right
    if type_item == 'cheap':
        if ratings[i] < ratings[entry_point]:
            right += ratings[i]
    else:
        if ratings[i] >= ratings[entry_point]:
            right += ratings[i]
bigger = max(left,right)
position = ''
if bigger == left:
    position = "Left"
else:
    position = "Right"
print(f"{position} - {bigger}")

"""
-2 2 1 5 9 3 2 -2 1 -1 -3 3
7
expensive
"""