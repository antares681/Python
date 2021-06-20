rows, cols = [int(el) for el in input().split()]
mx = [[int(el) for el in input().split()] for el in range(rows)]

# [
# [1 5 5 2 4],
# [2 1 4 14 3],
# [3 7 11 2 8],
# [4 8 12 16 4]
#   ]

max_so_far = None
max_start_i, max_start_j = 0, 0

curr_sum = []
for i in range(rows - 2):
    for j in range(cols -2):
        curr_sum = sum([
            mx[i][j], mx[i][j + 1], mx[i][j + 2],
            mx[i + 1][j], mx[i + 1][j + 1], mx[i + 1][j + 2],
            mx[i + 2][j], mx[i + 2][j + 1], mx[i + 2][j + 2]])

        if max_so_far is None or max_so_far < curr_sum:
            max_so_far = curr_sum
            max_start_i, max_start_j = i, j

print(f'Sum = {max_so_far}')
for i in range (3):
    for j in range(3):
        print(mx[max_start_i + i][max_start_j + j], end= ' ')
    print()

