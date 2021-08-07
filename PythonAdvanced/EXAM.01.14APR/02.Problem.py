from math import ceil
def position_chk(row, col):
    if row in range(7) and col in range(7):
        return True
    return False

def is_digit(el):
    try:
        return int(el)
    except Exception:
        return False

#DEFINE DATA
N= 7
player_1, player_2 = input().split(',')
points = {player_1: 501, player_2: 501}
board = []
for _ in range(N):
    board.append(input().split())

players_turn = {0: player_2, 1: player_1}
turns_count = 0

#START PROGRAM

while True:
    row, col = [el for el in input()[1:-1].split(', ')]
    row, col = int(row), int(col)
    turns_count += 1
    if position_chk(row, col):
        number = is_digit(board[row][col])
        if number:
            points[players_turn[turns_count % 2]] -= number

        current_points = sum([
            int(board[0][col]),
            int(board[-1][col]),
            int(board[row][0]),
            int(board[row][-1])
        ])

        if board[row][col] == 'D':
            points[players_turn[turns_count % 2]] -= current_points * 2
        if board[row][col] == 'T':
            points[players_turn[turns_count % 2]] -= current_points * 3
        if board[row][col] == 'B':
            print(f'{players_turn[turns_count % 2]} won '
                  f'the game with {ceil(turns_count/2)} throws!')
            exit(0)

        if points[player_1] <= 0 or points[player_2] <=0:
            break

print(f'{players_turn[turns_count % 2]} won '
                  f'the game with {ceil(turns_count/2)} throws!')


#TODO TEST INPUTS

# Ivan, Peter
# 12 21 18 4 20 7 11
# 9 D D D D D 10
# 15 D T T T D 3
# 2 D T B T D 19
# 17 D T T T D 6
# 22 D D D D D 14
# 5 8 23 13 16 1 24
# (3, 3)

# George, Hristo
# 17 8 21 6 13 3 24
# 16 D D D D D 14
# 7 D T T T D 15
# 23 D T B T D 2
# 9 D T T T D 22
# 19 D D D D D 10
# 12 18 4 20 5 11 1
# (1, 0)
# (2, 3)
# (0, 0)
# (4, 2)
# (5, 1)
# (3, 1)
# (0, 0)
# (2, 3)
