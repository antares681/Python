groceries_list = input().split('!')
command = input()
while not command == 'Go Shopping!':
    detailed_command = command.split(' ')
    if 'Urgent' in command:        # TEST 0
        item = detailed_command[1]
        if item not in groceries_list:
            groceries_list.insert(0, item)

    elif 'Unnecessary' in command:  # TEST 1
        item = detailed_command[1]
        if item in groceries_list:
            groceries_list.remove(item)

    elif 'Correct' in command:      # TEST 2
        old_name = detailed_command[1]
        new_name = detailed_command[2]
        if old_name in groceries_list:
            wanted_index = groceries_list.index(old_name)
            groceries_list[wanted_index] = new_name

    elif 'Rearrange' in command:    # TEST 3
        item = detailed_command[1]
        if item in groceries_list:
            groceries_list.remove(item)
            groceries_list.append(item)

    command = input()

joined_list = ', '.join(groceries_list)
print(joined_list)