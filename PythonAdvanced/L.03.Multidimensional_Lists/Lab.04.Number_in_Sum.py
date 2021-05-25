present = False
n = input()

if n and n.isdigit():
    n= int(n)
    matrix = [[el for el in input()] for el in range(n)]
    symbol = input()

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == symbol:
                print(f'{i, j}')
                present = True
                break
        if present:
            break
else:
    exit(0)
if not present:
    print(f'{symbol} does not occur in the matrix')