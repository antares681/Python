def update_kinghts(i1, j1, i2, j2):
    if not is_valid(j2,j1):
        return
    if not (i2, j2) in knights_database:
        knights_database[(i2,j2)] = []
    knights_database[(i2, j2)].append((i1,j1))

    if not (i1, j1) in knights_database:
        knights_database[(i1,j1)] = []
    knights_database[(i1, j1)].append((i2,j2))



def is_valid(i, j):
    if board_size <= i < 0 or board_size <= j < 0:
        return False
    if chess_board[i][j] == 'K':
        return #will return True or False if board




# TODO POSSIBLE MOVES SCHEME
possible_moves = (
    (-1,-2),
    (-1, 2),
    (-1,-2),
    (1, 2),
    (2, 1),
    (2,-1),
    (-2,1),
    (-2,-2),
)

knights_database = {}

# TODO CONSTRUCT EMPTY BOARD
board_size = int(input())
chess_board = [['0']* board_size for i in range(board_size)]

# TODO FILL THE BOARD
for i in range(board_size):
    row = list(input())

    for j in range(board_size):
        x = row[j]
        if row[j] == 'K':
            chess_board[i][j] = 'K'

            for move_i, move_j in possible_moves:
                i1, j1, i2, j2 = i, j, i + move_i, j + move_j

                # k1 = chess_board[i][j]
                # K2 =[i+move_i][j + move_j]
                update_kinghts(i1, j1, i2, j2)


print(chess_board)