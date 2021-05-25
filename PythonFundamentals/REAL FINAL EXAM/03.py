def userChecker(user, users):
    if user in users:
        return True
    return False

user_list = {}
data = input()

while not data == 'Statistics':
    user_data = data.split('->')
    user_action, username = user_data[0], user_data[1]
    if user_action == 'Add':
        if not userChecker(username, user_list):
            user_list[username] = []
        else:
            print(f'{username} is already registered')

    elif user_action =='Send':
        if userChecker(username, user_list):
            email = user_data[2]
            user_list[username].append(email)

    elif user_action == 'Delete':
        if userChecker(username, user_list):
           user_list.pop(username)
        else:
            print(f'{username} not found!')
    data = input()
print(f'Users count: {len(user_list)}')

for k, v in sorted(user_list.items(), key=lambda x: (x[len([1])], x[0])):
    print(f'{k}')
    for el in v:
        print(f' - {el}')