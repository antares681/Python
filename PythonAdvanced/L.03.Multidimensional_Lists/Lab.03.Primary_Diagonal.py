size = int(input())
diagonal_sum = 0

for i in range(size):
    row = [int(el) for el in input().split(' ')]
    diagonal_sum += row[i]
print(diagonal_sum)