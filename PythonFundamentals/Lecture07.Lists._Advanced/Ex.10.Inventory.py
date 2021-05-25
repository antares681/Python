journal = input().split(', ')
command = ''

while True:
    command = input().split(' - ')

    if command[0] == 'Craft!':
        break

    else:
        if command[0] == 'Collect' and command[1] not in journal:
            journal.append(command[1])
        elif command[0] == 'Drop' and command[1] in journal:
            journal.remove(command[1])

        elif command[0] == 'Combine Items':
            swap_list = command[1].split(':')
            if swap_list[0] in journal:
                journal.insert(journal.index(swap_list[0])+1, swap_list[1])

        elif command[0] == 'Renew' and command[1] in journal:
            journal.remove(command[1])
            journal.append(command[1])
print(', '.join(journal))

