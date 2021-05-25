targets_sequence = [int(el) for el in input().split()]

while True:
    command = input().split()
    if command[0] == 'End':
        break

    if command[0] == 'Shoot':
        if 0 <= int(command[1]) < len(targets_sequence):
            targets_sequence[int(command[1])] -= int(command[2])
            if targets_sequence[int(command[1])] <= 0:
                targets_sequence.pop(int(command[1]))

    elif command[0] == 'Add':
        if 0 <= int(command[1]) < len(targets_sequence):
            target_index = int(command[1])
            target_value = int(command[2])
            targets_sequence.insert(target_index, target_value)
        else:
            print('Invalid placement!')

    elif command[0] == "Strike":
        target_index = int(command[1])
        radius = int(command[2])
        if 0 <= target_index - radius and target_index + radius < len(targets_sequence):
            del targets_sequence[target_index-radius:target_index+radius+1]
        else:
            print('Strike missed!')

print("|".join([str(el) for el in targets_sequence]))