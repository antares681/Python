# SOLUTION 20/100
def matrix_contructor():
    rows, cols = [int(x) for x in input().split(', ')]
    matrix = [[int(el) for el in input().split(', ')] for _ in range(rows)]
    return matrix, rows, cols


def square_getter(matrix, rows, cols):
    all_squares = []
    for i in range(rows - 1):
        for j in range(cols - 1):
            all_squares.append([matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]])
    return all_squares


def matrix_crawler(squares):
    max_square = []
    max_square = max([squares[matrix] for matrix in range(len(squares)) if sum(max_square) < sum(squares[matrix])])
    return max_square


matrix, rows, cols = matrix_contructor()
squares = square_getter(matrix, rows, cols)
result = matrix_crawler(squares)

l1, l2 = result[:2], result[2:]
print(" ".join([str(el) for el in l1]))
print(" ".join([str(el) for el in l2]))
print(sum(result))

# SOLUTION DONCHO 100$
# def read_matrix(is_test=False):
#     if is_test:
#         return [
#             [7, 1, 3, 3, 2, 1],
#             [1, 3, 9, 8, 5, 6],
#             [4, 6, 7, 9, 1, 0],
#         ]
#     else:
#         (rows_count, columns_count) = map(int, input().split(', '))
#         matrix = []
#         for row_index in range(rows_count):
#             row = [int(x) for x in input().split(', ')]
#             matrix.append(row)
#         return matrix
#
#
# def get_sum_of_submatrix(matrix, row_index, column_index, size):
#     the_sum = 0
#     for r in range(row_index, row_index + size):
#         for c in range(column_index, column_index + size):
#             the_sum += matrix[r][c]
#     return the_sum
#
#
# def get_best_submatrix_sum_coordinates(matrix, submatrix_size):
#     best_row_index = 0
#     best_column_index = 0
#     best_sum = get_sum_of_submatrix(matrix, 0, 0, submatrix_size)
#
#     for row_index in range(len(matrix) - submatrix_size + 1):
#         for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
#             current_sum = get_sum_of_submatrix(matrix, row_index, col_index, submatrix_size)
#             if best_sum < current_sum:
#                 best_sum = current_sum
#                 best_row_index = row_index
#                 best_column_index = col_index
#     return (best_row_index, best_column_index)
#
#
# def print_result(coordinates, size):
#     (row_index, col_index) = coordinates
#     for r in range(row_index, row_index + size):
#         row = []
#         for c in range(col_index, col_index + size):
#             row.append(matrix[r][c])
#         print(' '.join(str(x) for x in row))
#     print(get_sum_of_submatrix(matrix, row_index, col_index, size))
#
#
# SUBMATRIX_SIZE = 2
#
# matrix = read_matrix()
# coordinates = get_best_submatrix_sum_coordinates(matrix, SUBMATRIX_SIZE)
# print_result(coordinates, SUBMATRIX_SIZE)
