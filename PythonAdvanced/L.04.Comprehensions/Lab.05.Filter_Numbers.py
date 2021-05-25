# divisors = [int(el) for el in range(2, 11)]
# start_idx, end_idx = int(input()), int(input())
# nmbr_range = [int(el) for el in range(start_idx, end_idx+1)]
# result = []
#
# for el in nmbr_range:
#     for elem in divisors:
#         if el % elem == 0:
#             result.append(el)
#             break
#
# print(result)

divisors = [int(el) for el in range(2, 11)]
nmbr_range = [int(el) for el in range(int(input()), int(input())+1)]
result = []
print([[el for el in nmbr_range if el % elem for elem in divisors == 0] for _ in range(divisors)])

for el in nmbr_range:
    for elem in divisors:
        if el % elem == 0:
            result.append(el)
            break
print(result)
