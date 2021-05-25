# def create_file(*args):
#     file_name = args[0]
#     with open(file_name, 'w') as file:
#         file.write('')
#
# def add_file(*args):
#     file_name, content = args[0], args[1]
#     with open(file_name, 'a') as file:
#         file.write(f'{content}\n')
#
# def replace_content(*args):
#     file_name, old_string, new_string = args[0], args[1], args[2]
#     with open(file_name, 'r+') as file:
#         data = ''.join(file.readlines())
#     ##TODO - MY WAY and extra with open(xx, 'w')
#     # with open(file_name, 'w') as file:
#     #     data = data.replace(old_string, new_string)
#     #     file.writelines(data)
#     ##TODO INES WAY - FILE.SEEK(0)
#         data = data.replace(old_string, new_string)
#         file.seek(0)
#         file.writelines(data)
#
# def delete_file(*args):
#     file_name = args[0]
#     os.remove(file_name)
#
#
# import os
#
# events_map = {
#         'Create':create_file,
#         'Add': add_file,
#         'Replace': replace_content,
#         'Delete':  delete_file
# }
#
# command = input()
# while not command == 'End':
#     event, *args = command.split('-')
#     try:
#         events_map[event](*args)
#         # if event == 'Create':
#         #     create_file(*args)
#         # elif event == 'Add':
#         #     add_file(*args)
#         # elif event == 'Replace':
#         #     replace_content(*args)
#         # elif event == 'Delete':
#         #     delete_file(*args)
#     except FileNotFoundError:
#        # print(f'Command {event} cannot be actioned File not found!')
#         print(f'An error occurred')
#     command = input()

#CLEAN SOLUTION:

def create_file(*args):
    file_name = args[0]
    with open(file_name, 'w') as file:
        file.write('')

def add_file(*args):
    file_name, content = args[0], args[1]
    with open(file_name, 'a') as file:
        file.write(f'{content}\n')

def replace_content(*args):
    file_name, old_string, new_string = args[0], args[1], args[2]
    with open(file_name, 'r+') as file:
        data = ''.join(file.readlines())
        data = data.replace(old_string, new_string)
        file.seek(0)
        file.writelines(data)

def delete_file(*args):
    file_name = args[0]
    os.remove(file_name)


import os
events_map = {'Create':create_file, 'Add': add_file,'Replace': replace_content,'Delete': delete_file}

command = input()
while not command == 'End':
    event, *event_details = command.split('-')
    try:
        events_map[event](*event_details)
    except FileNotFoundError:
        print(f'An error occurred')
    command = input()


'''
Create-file.txt
Add-file.txt-First Line
Add-file.txt-Second Line
Replace-random.txt-Some-some
Replace-file.txt-First-1st
Replace-file.txt-Second-2nd
Delete-random.txt
Delete-file.txt
End

'''