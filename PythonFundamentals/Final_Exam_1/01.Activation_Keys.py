raw_key = input()
command = input()

while not command == 'Generate':
    command = command.split('>>>')
    if command[0] == 'Contains':            # OK  Contains>>>def
        substring = command[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command[0] == 'Flip':              # OK  Flip>>>Upper>>>3>>>14
        start_idx, end_idx = command[2:]
        if command[1] == 'Upper':
            raw_key = raw_key[:int(start_idx)] + raw_key[int(start_idx):int(end_idx)].upper() + raw_key[int(end_idx):]
        elif command[1] == 'Lower':
            raw_key = raw_key[:int(start_idx)] + raw_key[int(start_idx):int(end_idx)].lower() + raw_key[int(end_idx):]
        print(raw_key)
    elif command[0] == 'Slice':
        start_idx, end_idx = command[1:]
        raw_key = raw_key[:int(start_idx)] + raw_key[int(end_idx):]
        print(raw_key)
    command = input()
print(f"Your activation key is: {raw_key}")


























# raw_key = str(input())
# command = input()
#
# while not command == 'Generate':
#     command = command.split('>>>')
#     if command[0] == 'Contains':
#         if command[1] in raw_key:
#             print(f"{raw_key} contains {command[1]}")
#         print(f'Substring not found!')
#     elif command[0] == 'Flip':
#         for i in range(int(command[2]), int(command[3])):
#                raw_key = raw_key.replace(raw_key[i], raw_key[i].swapcase())
#         print(raw_key)
#
#     elif command[0] == 'Slice':
#         for i in range(int(command[1]), int(command[2])):
#             raw_key = raw_key.replace(raw_key[i], '@')
#         raw_key = raw_key.replace('@',"")
#         print(raw_key)
#     command = input()
#
# print(f"Your activation key is: {raw_key}")