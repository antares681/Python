row = int(input())
matrix = []
[matrix.append(list(input()))for _ in range(row)]
col = row
current_damage = 0
position = []
removed = 0
def total_damage(matrix,row,col):
    count = 0
    if row - 2 >= 0 and col - 1 >= 0:
        if matrix[row-2][col-1] == "K":
            count += 1
    if row - 2 >= 0 and col + 1 < len(matrix):
        if matrix[row-2][col+1] == "K":
            count += 1
    if row + 2 < len(matrix) and col + 1 < len(matrix):
        if matrix[row+2][col+1] == "K":
            count += 1
    if row + 2 < len(matrix) and col - 1 >= 0:
        if matrix[row+2][col-1] == "K":
            count += 1
    if col - 2 >= 0 and row + 1 < len(matrix):
        if matrix[row+1][col-2] == "K":
            count += 1
    if col - 2 >= 0 and row - 1 >= 0:
        if matrix[row-1][col-2] == "K":
            count += 1
    if col + 2 < len(matrix) and row + 1 < len(matrix):
        if matrix[row+1][col+2] == "K":
            count += 1
    if col + 2 < len(matrix) and row - 1 >= 0:
        if matrix[row-1][col+2] == "K":
            count += 1
    return count



while True:
    for row_index in range(row):
        for col_index in range(col):
            if matrix[row_index][col_index] == "K":
                calculated_damage = total_damage(matrix,row_index,col_index)
                if calculated_damage > current_damage:
                    current_damage = calculated_damage
                    position = [row_index,col_index]
    if current_damage == 0:
        break
    else:
        matrix[position[0]][position[1]] = "0"
        current_damage = 0
        removed += 1
        position = []
print(removed)

#SOLUTION EXCERCISE
# def read_board():
#     matrix = []
#     n = int(input())
#
#     for _ in range(n):
#         matrix.append(list(input()))
#
#     return matrix
#
#
# def knights_are_attacking_each_other(matrix):
#     knight_positions = find_all_knights(matrix)
#
#     for row, col in knight_positions:
#         positions_to_check = [
#             (row - 2, col + 1),
#             (row - 1, col + 2),
#             (row + 1, col + 2),
#             (row + 2, col + 1),
#             (row + 2, col - 1),
#             (row + 1, col - 2),
#             (row - 1, col - 2),
#             (row - 2, col - 1),
#         ]
#
#         for position in positions_to_check:
#             pos_row, pos_col = position
#
#             if not (0 <= pos_row <= len(matrix) - 1):
#                 continue
#             if not (0 <= pos_col <= len(matrix) - 1):
#                 continue
#             if matrix[pos_row][pos_col]  == 'K':
#                 return True
#
#     return False
#
#
# def find_all_knights(matrix):
#     positions = []
#
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if matrix[i][j] == 'K':
#                 positions.append((i, j))
#
#     return positions
#
#
# def calculate_aggression(matrix, knight_positions):
#     aggression_scores = {}
#     for pos in knight_positions:
#         row, col = pos
#         positions_to_check = [
#             (row - 2, col + 1),
#             (row - 1, col + 2),
#             (row + 1, col + 2),
#             (row + 2, col + 1),
#             (row + 2, col - 1),
#             (row + 1, col - 2),
#             (row - 1, col - 2),
#             (row - 2, col - 1),
#         ]
#
#         attacked_count = 0
#         for attacked_row, attacked_col in positions_to_check:
#             if not (0 <= attacked_row <= len(matrix) - 1):
#                 continue
#             if not (0 <= attacked_col <= len(matrix) - 1):
#                 continue
#             if matrix[attacked_row][attacked_col]  == 'K':
#                 attacked_count += 1
#
#         aggression_scores[(row, col)] = attacked_count
#
#     return aggression_scores
#
#
# def find_max_aggression(aggression_scores):
#     max_so_far = None
#     max_pos = None
#
#     for pos, aggression in aggression_scores.items():
#         if max_so_far is None or max_so_far < aggression:
#             max_so_far = aggression
#             max_pos = pos
#
#     return max_pos
#
#
# def main():
#     matrix = read_board()
#
#     deleted_knights_count = 0
#     while knights_are_attacking_each_other(matrix) is True:
#         knight_positions = find_all_knights(matrix)  # [(0, 0), (1, 1)]
#         aggression_scores = calculate_aggression(matrix, knight_positions)  # {(0, 0): 5}
#
#         row, col = find_max_aggression(aggression_scores)
#
#         matrix[row][col] = '0'
#         deleted_knights_count += 1
#
#     print(deleted_knights_count)