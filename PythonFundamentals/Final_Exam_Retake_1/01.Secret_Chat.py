concealed_message = input()

command = input()

while not command == 'Reveal':
    command = command.split(':|:')
    instruction = command[0]

    if instruction == 'InsertSpace':
        idx = int(command[1])
        concealed_message = concealed_message[:idx] + " " + concealed_message[idx:]
    elif instruction == 'Reverse':
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1) + substring[::-1]
        else:
            print('error')
            command = input()
            continue
    elif instruction == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
    print(concealed_message)
    command = input()

print(f"You have a new text message: {concealed_message}")