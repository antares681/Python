sugar_cubes = input().split(" ")
command = input()


while not command == 'Mort':
    command = command.split()
#CHECK 1
    if command[0] == 'Add': #TEST #1 4 5 19 13 42 69 24
        value = command[1]
        sugar_cubes.append(value)
#CHECK 2
    if command[0] == 'Remove': #TEST 1 4 5 24 13 42 24 24
        value = command[1]
        sugar_cubes.remove(value)

    if command[0] == 'Replace':  #TEST 1 4 5 19 13 1 69 1
        value = command[1]
        replacement = command[2]
        sugar_cubes.insert(sugar_cubes.index(value), replacement)
        sugar_cubes.remove(value)

    if command[0] == 'Collapse': #TEST 1 4 5 19 4 4 69 24
        value = command[1]
        sugar_cubes = [str(element) for element in sugar_cubes if int(element) >= int(value)]

    command = input()

print(' '.join(sugar_cubes))


#TEST INPUT
# 1 4 5 19 13 42 69 24
# Add 1
# Remove 4
# Replace 1 26
# Mort