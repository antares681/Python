from collections import deque
names = deque()
dispencer = int(input())


def gatherList(names):
    data = input()
    while not data == 'Start':
        names.append(data)
        data = input()
    return names


def solve(names, dispencer):
    command = input()
    while not command == 'End':
        command = command.split()
        if command[0] == 'refill':
            dispencer+= int(command[1])
        else:
            water_for_person = int(command[0])
            name = names.popleft()
            if water_for_person <= dispencer:
                dispencer -= water_for_person
                print(f'{name} got water')
            else:
                print(f'{name} must wait')
        command = input()
    print(f'{dispencer} liters left')

names = gatherList(names)
solve(names, dispencer)