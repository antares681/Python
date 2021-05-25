shopping_list = input().split("!")
command = input()

while not command == 'Go Shopping!':
    command = command.split()
    if command[0] == 'Urgent':
        if command[1] not in shopping_list:
            shopping_list.insert(0, command[1])

    elif command[0] == 'Unnecessary':
        if command[1] in shopping_list:
            shopping_list.remove(command[1])

    elif command[0] == 'Correct':
        while command[1] in shopping_list:
            item_to_rmv_idx = shopping_list.index(command[1])
            shopping_list.remove(command[1])
            shopping_list.insert(item_to_rmv_idx, command[2])

    elif command[0] == 'Rearrange':
        for element in shopping_list:
            if element == command[1]:
                item = shopping_list.pop(shopping_list.index(command[1]))
                shopping_list.append(item)
    command = input()

print(', '.join(shopping_list))