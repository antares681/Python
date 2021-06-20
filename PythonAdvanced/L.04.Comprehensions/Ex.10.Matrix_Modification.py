mx_size = int(input())
mx = [list(map(int, input().split())) for el in range(mx_size)]

data = input()
while not data == 'END':
    command, row, col, val = data.split()
    row, col, val = int(row), int(col), int(val)
    if  0 <= row < mx_size and 0 <= col < mx_size:
        if command == 'Add':
            mx[row][col] += val
        elif command == 'Subtract':
            mx[row][col] -= val
    else:
        print(f'Invalid coordinates')
    data = input()


from pprint import pprint

mx= [[i for i in range(10)] for _ in range(10)]



pprint(mx)
# [print(' '.join(map(str,i))) for i in mx]