def diagonal_crawler(mx):
    diagonal_sum_1, diagonal_sum_2 = 0, 0

    for i in range(len(mx)):
        diagonal_sum_1 += mx[i][i]

    y = len(mx)-1
    for x in range(len(mx)):
        diagonal_sum_2 += mx[x][y]
        y-=1
    result = abs(diagonal_sum_1 - diagonal_sum_2)
    return result



n = int(input())
matrix = [[int(el) for el in input().split(' ')] for _ in range(n)]
print(diagonal_crawler(matrix))

