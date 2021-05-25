#solution 1
#
# digit = int(input())
#
# for num in range(1, digit + 1):
#     digit_list = list(map(int, str(num)))
#     digit_sum = 0
#     for elements in digit_list:
#         digit_sum += int(elements)
#
#     if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
#         print(f'{num} -> True')
#     else:
#         print(f'{num} -> False')

#solution 2

digit = int(input())

for num in range(1, digit + 1):
    digit_sum = 0
    elements = num
    while elements > 0:
        digit_sum += elements % 10
        elements = int(elements / 10)
    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')