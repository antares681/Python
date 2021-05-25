our_word = input()
command = input()
while command != 'Done':
    command = command.split()
    if command[0] == 'TakeOdd':
        our_word = ''.join([our_word[index] for index in range(len(our_word)) if index % 2 != 0])
        print(our_word)
    elif command[0] == 'Cut':
        index, length = int(command[1]), int(command[2])
        removal_string = our_word[index:index+length]
        our_word = our_word.replace(removal_string,'',1)
        print(our_word)

    elif command[0] == 'Substitute':
        substring, substitute = command[1], command[2]
        if substring in our_word:
            our_word = our_word.replace(substring, substitute)
            print(our_word)
        else:
            print("Nothing to replace!")

    command = input()

print(f'Your password is: {our_word}')