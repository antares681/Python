# version_number = input().split(".")
# print(version_number)
#
# x = int(version_number[0])
# y = int(version_number[1])
# z = int(version_number[2])
#
# if z + 1 <=9:
#     z = z + 1
# else:
#     z = 0
#     if y + 1 <=9:
#         y = y +1
#     else:
#         y = 0
#         x = x + 1
#
# print(f'{x}.{y}.{z}')

# version_number = input().split(".")
#
# x = int(version_number[0])
# y = int(version_number[1])
# z = int(version_number[2])
#
# if z + 1 <=9:
#     version_number.pop(2)
#     version_number.insert(2, z+1)
# else:
#     version_number[2] = 0
#     if y + 1 <=9:
#         version_number.pop(1)
#         version_number.insert(1, y + 1)
#     else:
#         version_number[1] = 0
#         version_number.pop(0)
#         version_number.insert(0, x + 1)
#
# print(f'{version_number[0]}.{version_number[1]}.{version_number[2]}')

version_number = input().split(".")
version_number_result = version_number.copy()

if int(version_number_result[2]) + 1 <= 9:
    version_number_result.pop(2)
    version_number_result.insert(2, int(version_number[2]) + 1)
else:
    version_number_result[2] = 0
    if int(version_number[1]) + 1 <= 9:
        version_number_result.pop(1)
        version_number_result.insert(1, int(version_number[1]) + 1)
    else:
        version_number_result[1] = 0
        version_number_result.pop(0)
        version_number_result.insert(0, int(version_number[0]) + 1)

print(f'{version_number_result[0]}.{version_number_result[1]}.{version_number_result[2]}')
