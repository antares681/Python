from itertools import chain
rows, cols = [int(el) for el in input().split()]
mx = [[int(el) for el in input().split()] for el in range(rows)]
squares = []
for r in range(rows - 2):
    for c in range(cols - 2):
        squares.append([
                        [mx[r][c], mx[r][c + 1], mx[r][c + 2]],
                        [mx[r + 1][c], mx[r + 1][c + 1], mx[r + 1][c + 2]],
                        [mx[r + 2][c], mx[r + 2][c + 1], mx[r + 2][c + 2]],
                        ])
max_square = []
for el in squares:
    if sum(chain(*el)) > sum(chain(*max_square)):
        max_square = el

print(f"Sum = {sum(chain(*max_square))}")
for el in max_square:
    print(' '.join([str(elem) for elem in el]))


##TODO  SOLUTION MIVKATA

# def sum_sub_matrix(m, r, c):
#     return m[r][c] + m[r][c + 1] + m[r + 1][c] + m[r + 1][c + 1] +m[r + 2][c] + m[r][c + 2]\
#            + m[r + 2][c + 2] + m[r + 2][c + 1] + m[r + 1][c + 2]

# rows, columns = map(int, input().split(" "))
# matrix = []
#
# for i in range(rows):
#     row = list(map(int, input().split(" ")))
#     matrix.append(row)
#
# max_sum, max_r, max_c = 0, 0, 0
#
# for row in range(rows - 2):
#     for col in range(columns - 2):
#         current_sub_sum = sum_sub_matrix(matrix, row, col)
#         if current_sub_sum > max_sum:
#             max_r = row
#             max_c = col
#             max_sum = current_sub_sum
#
# if matrix:
#     print(f"Sum = {max_sum}")
#     print(f'{matrix[max_r][max_c]} {matrix[max_r][max_c + 1]} {matrix[max_r][max_c + 2]}')
#     print(f'{matrix[max_r + 1][max_c]} {matrix[max_r + 1][max_c + 1]} {matrix[max_r + 1][max_c + 2]}')
#     print(f"{matrix[max_r + 2][max_c]} {matrix[max_r + 2][max_c + 1]} {matrix[max_r + 2][max_c + 2]}")