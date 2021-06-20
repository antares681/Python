def read_matrix():
    size = int(input())
    matrix = []
    for _ in range(size):
        matrix.append([int(a) for a in input().split()])
    return matrix

def boom(m, row, col):
    power = m[row][col]
    direction_x = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    direction_y = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    if m[row][col] == 0:
        return
    for i in range(len(direction_y)):
        move_y = row + direction_y[i]
        move_x = col + direction_x[i]
        if 0 <= move_y < len(m) and 0 <= move_x < len(m):
            if m[move_y][move_x] > 0:
               m[move_y][move_x] -= power

matrix = read_matrix()
bombs_coords = [list(map(int, c.split(','))) for c in input().split()]

while bombs_coords:
    y, x = bombs_coords.pop(0)
    boom(matrix, y, x)

alive_cells = 0
alive_sum = 0
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if matrix[row][col] > 0:
            alive_cells += 1
            alive_sum += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_sum}")
for row in matrix:
    print(*row)


#TODO SOLUTION 2

matrix = []
for _ in range(int(input())):
    matrix.append([int(i) for i in input().split(" ")])
bombs = input().split(" ")
def damage(m,row,col):
    bomb_damage = m[row][col]
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if not (i in range(len(matrix)) and (j in range(len(matrix)))):
                continue
            m[i][j] -= bomb_damage if m[i][j] > 0 else 0
    m[row][col] = 0
    return m
while bombs:
    bomb = bombs.pop(0)
    bomb = bomb.split(",")
    bomb_row, bomb_col = map(int,bomb)
    if matrix[bomb_row][bomb_col] > 0:
        matrix = damage(matrix, bomb_row, bomb_col)
survived = [char for i in range(len(matrix)) for char in matrix[i] if char > 0]
print(f"Alive cells: {len(survived)}")
print(f"Sum: {sum([int(i) for i in survived])}")
[print(*sub) for sub in matrix]