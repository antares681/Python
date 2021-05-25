encrypted_message = input()
command = input()

while not command == 'Decode':
    command = command.split('|')
    action = command[0]

    if action == 'Move':
        nmbr_letters = int(command[1])
        encrypted_message = encrypted_message[nmbr_letters:] + encrypted_message[:nmbr_letters]
    elif action == 'Insert':
        index, value = command[1:]
        index, value = int(index), value
        encrypted_message= encrypted_message[:index] + value + encrypted_message[index:]
    elif action == 'ChangeAll':
        substring, replacement = command[1:]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {encrypted_message}")