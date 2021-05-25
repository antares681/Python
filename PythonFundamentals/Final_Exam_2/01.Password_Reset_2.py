def input_data():
    pwd = input()
    data = input()
    while not data == 'Done':
        new_pwd = command_analyzer(pwd, data)
        if new_pwd:
            pwd = new_pwd
            print(pwd)
        data = input()
    return pwd

def command_analyzer(pwd, command):
    command = command.split(' ')
    if command[0] == 'TakeOdd':
        pwd = oddCalculator(pwd)

    elif command[0] == 'Cut':
        idx, length = int(command[1]), int(command[2])
        pwd = cutter(pwd, idx, length)

    elif command[0] == 'Substitute':
        substr, subst = command[1], command[2]
        pwd = substituter(pwd, substr, subst)
    return pwd

def oddCalculator(pwd):
    str_to_list = [el for el in pwd]
    pwd = (''.join([str_to_list[el] for el in range(len(str_to_list)) if not el % 2 == 0 ]))
    return pwd

def cutter(pwd, idx, length):
    substr = pwd[idx:idx+length]
    pwd = pwd.replace(substr,'',1)
    return pwd

def substituter(pwd, substr, subst):
    if substr in pwd:
        pwd = pwd.replace(substr, subst)
        return pwd
    else:
        print("Nothing to replace!")

print(f'Your password is: {input_data()}')