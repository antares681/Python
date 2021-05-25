#SOLUTION 1

# matrix_rows, matrix_cols = [int(el) for el in input().split(', ')]
# matrix = [[int(el) for el in input().split(' ')] for _ in range(matrix_rows)]

# for j in range(matrix_cols):
#     col_sum = 0
#     for i in range(matrix_rows):
#         col_sum += matrix[i][j]
#     print(col_sum)


#SOLUTION 2
matrix_rows, matrix_cols = [int(el) for el in input().split(', ')]
matrix = [[int(el) for el in input().split(' ')] for _ in range(matrix_rows)]
for j in range(matrix_cols):
    print(sum(row[j] for row in matrix))
