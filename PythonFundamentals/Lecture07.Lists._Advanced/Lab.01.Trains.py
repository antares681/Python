def wagon_manipulator(wagon_state):
    wagon_list = [0] * int(wagon_state)

    while not wagon_state[0] == "End":

        if wagon_state[0] == 'add':
            wagon_list = list(map(int, wagon_list))
            wagon_list[-1] += int(wagon_state[1])

        if wagon_state[0] == 'insert':
            wagon_list = list(map(int, wagon_list))
            wagon_list[int(wagon_state[1])] += int(wagon_state[2])

        if wagon_state[0] == 'leave':
            wagon_list = list(map(int, wagon_list))
            wagon_list[int(wagon_state[1])] -= int(wagon_state[2])

        wagon_state = input().split(" ")

    return wagon_list

wagons_number =  input()
print(wagon_manipulator(wagons_number))