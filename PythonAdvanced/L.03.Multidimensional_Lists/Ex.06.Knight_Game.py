def knight_perimeter_check(board_size, board, coor_x, coor_y, possible_moves):
    if 0 <= coor_x <= board_size and 0 <= coor_y <= board_size:
        for coor_x1, coor_y1 in possible_moves:
            k1 = board[coor_x][coor_y]
            k2 = [coor_x + coor_x1][coor_y + coor_y1]

            update_knights(coor_x, coor_y, coor_x1, coor_y1)

            print(coor_x + coor_x1, coor_y + coor_y1)

        # if 0 <= coor_x < board_size - 1 and 0 <= coor_y < board_size -1:
        #     board = check_down_vertical_right(board, coor_x, coor_y)
        # elif 0 <= coor_x < board_size - 2 and 0 <= coor_y < board_size -2:
        #     board = check_down_horizontal_right(board, coor_x, coor_y)
        #
        # if 2 <= coor_x < board_size - 2 and 2 <= coor_y < board_size -2:
        #     board = check_down_vertical_left(board, coor_x, coor_y)
        #     board = check_down_vertical_right(board, coor_x, coor_y)
        #     board = check_up_vertical_left(board, coor_x, coor_y)
        #     board = check_up_vertical_right(board, coor_x, coor_y)
        #     board = check_down_horizontal_left(board, coor_x, coor_y)
        #     board = check_down_horizontal_right(board, coor_x, coor_y)
        #     board = check_up_horizontal_left(board, coor_x, coor_y)
        #     board = check_up_horizontal_right(board, coor_x, coor_y)
    else:
        return board
    return board

#HORIZONTAL
def check_down_vertical_left(board, x, y):
    if board[x-1][y+2] == 'K':
        board[x-1][y+2] = 'X'
    return board
def check_down_vertical_right(board, x, y):
    if board[x+1][y+2] == 'K':
        board[x+1][y+2] = 'X'
    return board
def check_down_horizontal_left(board, x, y):
    if board[x-2][y+1] == 'K':
        board[x-2][y+1] = 'X'
    return board
def check_down_horizontal_right(board, x, y):
    if board[x+2][y+1] == 'K':
        board[x+2][y+1] = 'X'
    return board

#VERTICAL
def check_up_vertical_left(board, x, y):
    if board[x-1][y-2] == 'K':
        board[x-1][y-2] = 'X'
    return board
def check_up_vertical_right(board, x, y):
    if board[x+1][y-2] == 'K':
        board[x+1][y-2] = 'X'
    return board
def check_up_horizontal_left(board, x, y):
    if board[x-2][y-1] == 'K':
        board[x-2][y-1] = 'X'
    return board
def check_up_horizontal_right(board, x, y):
    if board[x+2][y-1] == 'K':
        board[x+2][y-1] = 'X'
    return board


'''
[
0K0K0
K000K
00K00
K000K
0K0K0
'''

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

#TODO CONSTRUCT BOARD
board_rows = []
chess_board =[]
board_size = int(input())
for i in range(board_size):
    board_rows.append(input())
for i in range(len(board_rows)):
    chess_board.append([symbol for symbol in board_rows[i]])
#START BOARD READY!
#print(chess_board)

#TODO ANALYZE_BOARD
knight_range = {}

for y in range(board_size):
    for x in range(board_size):
        knight_perimeter_check(board_size, chess_board, x, y, possible_moves)

for i in range(len(chess_board)):
    print(chess_board[i])