# SOLIUTION 1 - LOOPS

matrix_rows, matrix_cols = [int(el) for el in input().split(', ')]
matrix = []
ttl_sum =0
for i in range(matrix_rows):
    matrix.append([int(el) for el in input().split(', ')])
for el in matrix:
    ttl_sum += sum(el)
print(ttl_sum, matrix, sep='\n')

#
# #SOLUTION 2 - COMPRESHENSION
# rows, cols = [int(el) for el in input().split(', ')]
# matrix = []
# ttl_sum = 0
# for _ in range(rows):
#     row = [int(number) for number in input().split(', ')]
#     ttl_sum += sum(row)
#     matrix.append(row)
# print(ttl_sum, matrix, sep='\n')

# from itertools import chain
# rows, cols = [int(el) for el in input().split(', ')]
# matrix = [[int(number) for number in input().split(', ')] for _ in range(rows)]
# ttl_sum = sum(chain(*matrix))
# print(ttl_sum, matrix, sep='\n')