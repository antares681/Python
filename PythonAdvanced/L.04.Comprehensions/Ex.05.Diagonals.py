def create_row():
    row = input().split(', ')
    return [int(j) for j in row]


data = int(input())
mx = [create_row() for i in range(data)]

diag_1 = []
diag_1_sum =0
for i in range(len(mx)):
        diag_1.append(str(mx[i][i]))
        diag_1_sum += mx[i][i]

diag_2 = []
diag_2_sum =0
j = -1
for i in range(len(mx)):
        diag_2.append(str(mx[i][j]))
        diag_2_sum += mx[i][j]
        j+=-1

#OR
# digonal 1  is when i = j
# diagonal 2 is when j = n -1 - i
# first_diagonal = [mx[i][j]
#                   for i in range(data)
#                   for j in range(data)
#                   if i == j]
# second_diagonal = [mx[i][j] for i in range(data) for j in range(data) if data - 1 - i == j]


print(f'First diagonal: {", ".join(diag_1)}. Sum: {diag_1_sum}')
print(f'First diagonal: {", ".join(diag_2)}. Sum: {diag_2_sum}')
