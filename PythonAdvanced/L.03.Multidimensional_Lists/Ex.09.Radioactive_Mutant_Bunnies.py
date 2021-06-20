def field_constructor():
    #TODO CREATE FIELD
    rows, cols = map(int, input().split())
    mx = [['.' for x in range(cols)] for _ in range(rows)]
    print(mx)
    #TODO POPULATE FIELD WITH BUNNIES
    for i in range(rows):
        bunnies = input()
        for j in range(cols):
            if not bunnies[j] == ".":
                mx[i][j] = bunnies[j]
    return rows, cols, mx

# #TODO CALC PLAYER MOVEMENTS
def player_mover(step):
    movments = {'R': (0,-1), 'L': (0,1), 'U': (1, 0), 'D': (-1, 0)}
    i1, j1 = movments[step][0], movments[step][1]
    for i in range(rows):
        for j in range(cols):
            if lair[i][j] == 'P':
                if lair[i-i1][j-j1] == '.':
                    lair[i][j] = '.'
                    if i-i1 == -1 or j-j1 == -1:
                        is_winner = True
                        return is_winner, i, j
                    lair[i-i1][j-j1] = 'P'
                    return is_loser, i, j
                elif lair[i-i1][j-j1] == 'B':
                    return is_loser, i, j
    return None, i, j
# def bunny_multiplier():


from collections import deque
is_winner = False
is_loser = False

rows, cols, lair = field_constructor()

steps = deque(x for x in input())
print(steps)

for _ in range(len(steps)):
    step = steps.popleft()
    row, col = player_mover(step)
    print(lair)

    if is_winner:
        for el in lair:
            print(''.join(el))
        print(f'won: {row} {col}')
    if is_loser:
        for el in lair:
            print(''.join(el))
        print(f'lose: {row} {col}')

###
rows, cols = [int(x) for x in input().split()]


def read_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(list(input()))
    return matrix


def find_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'P':
                return [row, col]


def is_move_valid(row, col):
    return 0 <= row < rows and 0 <= col < cols


def player_move(row, col, direction):
    if direction == 'U':
        potential_row = row - 1
        potential_col = col
    elif direction == 'R':
        potential_col = col + 1
        potential_row = row
    elif direction == 'D':
        potential_row = row + 1
        potential_col = col
    elif direction == 'L':
        potential_col = col - 1
        potential_row = row

    if is_move_valid(potential_row, potential_col):
        matrix[row][col] = '.'
        if matrix[potential_row][potential_col] == 'B':
            return ('dead', potential_row, potential_col)
        matrix[potential_row][potential_col] = 'P'
        return potential_row, potential_col
    matrix[row][col] = '.'
    return 'won', row, col


def get_bunnies_indexes(matrix):
    bunnies = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'B':
                bunnies.append([i, j])

    return bunnies


def mutate_bunny(matrix, row, col, is_dead):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for position in directions:
        potential_row = row + position[0]
        potential_col = col + position[1]
        if is_move_valid(potential_row, potential_col):
            if matrix[potential_row][potential_col] == 'P':
                is_dead = True
                dead_row, dead_col = potential_row, potential_col
            matrix[potential_row][potential_col] = 'B'
    if is_dead:
        return is_dead, dead_row, dead_col


def bunnies_mutate(matrix, is_dead):
    result = None
    bunnies = get_bunnies_indexes(matrix)
    for bunny in bunnies:
        res = mutate_bunny(matrix, bunny[0], bunny[1], is_dead)
        if res:
            result = res
    return result


matrix = read_matrix(rows)
player_position = find_player(matrix)
commands = list(input())
is_dead = False

for direction in commands:
    res = player_move(player_position[0], player_position[1], direction)

    res_1 = bunnies_mutate(matrix, is_dead)
    if res_1:
        is_dead, row, col = res_1

    if res[0] == 'dead':
        for row in matrix:
            print(''.join(row))
        print(f'dead: {res[1]} {res[2]}')
        break
    elif res[0] == 'won':
        for row in matrix:
            print(''.join(row))
        print(f'won: {res[1]} {res[2]}')
        break
    else:
        player_position[0], player_position[1] = res[0], res[1]

    if is_dead:
        for _ in matrix:
            print(''.join(_))
        print(f'dead: {row} {col}')
        break

