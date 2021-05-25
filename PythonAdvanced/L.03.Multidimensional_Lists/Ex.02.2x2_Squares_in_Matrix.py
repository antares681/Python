rows, cols = [int(el) for el in input().split()]
matrix = [[el for el in input().split()] for _ in range(rows)]
duplicate_counter = {}
squares = []
for j in range(cols-1):
    for i in range(rows-1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            squares.append(matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1])

for el in range(len(squares)):
    if not squares[el] in duplicate_counter:
        duplicate_counter[squares[el]] = 1
    else:
        duplicate_counter[squares[el]] +=1

counter = 0
if duplicate_counter:
    for k, v in duplicate_counter.items():
        counter += v
print(counter)