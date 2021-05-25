data_string = input()

command = input()

while not command.strip() == "Finish":
    command = command.split()
    action = command[0]
    if action == 'Replace':
        curr_char, new_char = command[1], command[2]
        data_string = data_string.replace(curr_char, new_char)
        print(data_string)

    elif action =='Cut':
        start_idx, end_idx = int(command[1]), int(command[2])
        if start_idx in range(len(data_string)) and end_idx in range(len(data_string)):
            data_string = data_string[:start_idx] + data_string[end_idx+1:]
            print(data_string)
        else:
            print('Invalid indices!')
    elif action == 'Make':
        action_type = command[1]
        if action_type == 'Lower':
            data_string = data_string.lower()
        elif action_type == 'Upper':
            data_string = data_string.upper()
        print(data_string)

    elif action == 'Check':
        data_substr = command[1]
        if data_substr in data_string:
            print(f'Message contains {data_substr}')
        else:
            print(f"Message doesn't contain {data_substr}")

    elif action == 'Sum':
        start_idx, end_idx = int(command[1]), int(command[2])
        if start_idx in range(len(data_string)) and end_idx in range(len(data_string)):
            ascii_values = [ord(i) for i in data_string[start_idx:end_idx+1]]
            print(sum(ascii_values))
        else:
            print('Invalid indices!')
    command = input()