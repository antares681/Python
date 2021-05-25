#TASK COUNTER STRIKE

initial_energy = int(input())

distance = input()
counter_won_battles = 0
is_winner = True

while True:

    if distance == "End of battle":
        break
    distance = int(distance)

    if initial_energy - distance >= 0:
        initial_energy -= distance
        counter_won_battles += 1
        if counter_won_battles % 3 == 0:
            initial_energy += counter_won_battles
    else:
        is_winner = False
        print(f"Not enough energy! Game ends with {counter_won_battles} won battles and {initial_energy} energy")
        break

    distance = input()

if is_winner:
    print(f"Won battles: {counter_won_battles}. Energy left: {initial_energy}")

#TASK 2 - SOOT TO WIN
targets = [int(el) for el in input().split()]

index = input()
counter_shot_targets = 0

while not index == "End":
    index = int(index)

    if index not in range(len(targets)):
        index = input()
        continue

    current_value = targets[index]

    if current_value == -1:
        index = input()
        continue

    targets[index] = -1
    counter_shot_targets += 1

    for current_index in range(len(targets)):
        if targets[current_index] == -1:
            continue
        if targets[current_index] > current_value:
            targets[current_index] -= current_value
        else:
            targets[current_index] += current_value

    index = input()

print(f"Shot targets: {counter_shot_targets} -> {' '.join([str(el) for el in targets])}")

#TASK 2 - MOVING TARGETS - SEE OWN SOLUTION

def check_if_index_is_valid(index, len_list):
    if index in range(len_list):
        return True
    return False


targets = [int(el) for el in input().split()]

command_data = input()

while not command_data == "End":
    command, index, val = command_data.split()
    index = int(index)
    val = int(val)
    if command == "Shoot":
        if check_if_index_is_valid(index, len(targets)):
            targets[index] -= val
            if targets[index] <= 0:
                targets.pop(index)
    elif command == "Add":
        if check_if_index_is_valid(index, len(targets)):
            targets.insert(index, val)
        else:
            print("Invalid placement!")
    elif command == "Strike":
        left_most_index = index - val
        right_most_index = index + val
        if check_if_index_is_valid(index, len(targets)) and check_if_index_is_valid(left_most_index, len(
                targets)) and check_if_index_is_valid(right_most_index, len(targets)):
            left_unstriked_part = targets[:left_most_index]
            right_unstriked_part = targets[right_most_index + 1:]
            targets = left_unstriked_part + right_unstriked_part
        else:
            print("Strike missed!")

    command_data = input()

print('|'.join([str(el) for el in targets]))


#MEMORY GAMES
def check_index_is_valid(index, len_list):
    if index in range(len_list):
        return True
    return False


cards = input().split()

command = input()

number_of_rounds = 0

while not command == "end" and cards:
    index_1, index_2 = command.split()
    index_1 = int(index_1)
    index_2 = int(index_2)

    number_of_rounds += 1

    if check_index_is_valid(index_1, len(cards)) and check_index_is_valid(index_2,
                                                                          len(cards)) and not index_1 == index_2:
        el_1 = cards[index_1]
        el_2 = cards[index_2]
        if el_1 == el_2:
            cards.remove(el_1)
            cards.remove(el_2)
            print(f"Congrats! You have found matching elements - {el_1}!")
        else:
            print("Try again!")
    else:
        element_to_add = f"-{number_of_rounds}a"
        middle = len(cards) // 2
        cards.insert(middle, element_to_add)
        cards.insert(middle, element_to_add)
        print("Invalid input! Adding additional elements to the board")

    command = input()

if not cards:
    print(f"You have won in {number_of_rounds} turns!")
else:
    print("Sorry you lose :(")
    print(' '.join(cards))