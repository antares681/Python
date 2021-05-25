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



