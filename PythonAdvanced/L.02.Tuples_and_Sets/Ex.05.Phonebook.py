from collections import defaultdict
phonebook = defaultdict(str)
data = input()
while not data.isdigit():
    name, phone = data.split('-')
    phonebook[name] = phone
    data = input()

check_list_length = int(data)
for _ in range(check_list_length):
    name_to_check = input()
    if name_to_check in phonebook:
        print(f"{name_to_check} -> {phonebook[name_to_check]}")
    else:
        print(f'Contact {name_to_check} does not exist.')
