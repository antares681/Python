# #TODO Solution 1
# file = open('text.txt', 'r')
# file.close()

#TODO Solution 2 WITH is a CONTEXT manager closes the file automatically once command is finished
try:
    with open('text.txt', 'r') as file:
        print(file.readlines())
except FileNotFoundError:
    print('File not found')

#TODO USING SPLIT
try:
    with open('text.txt', 'r') as file:
        row1, row2 = file.readlines()
        print(row1, end= '')
        print(row2, end= '')
except FileNotFoundError:
    print('File not found')