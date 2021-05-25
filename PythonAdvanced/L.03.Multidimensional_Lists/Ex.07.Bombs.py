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