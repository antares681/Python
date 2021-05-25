# nums_list = list(map(int, input().split(", ")))
# list_result = [nums_list.index(element) for element in nums_list if element % 2 == 0]
# print(list_result)

# nums = [int(el) for el in input().split(', ')]
# even_nums = [num for num in range(len(nums)) if nums[num] % 2 == 0]
# print(even_nums)

# list_result = []
# nums_list = input().split(", ")
# print(nums_list)
# for element in range(len(nums_list)):
#      if int(nums_list[element]) % 2 == 0:
#         list_result.append(nums_list[element])
# print(list_result)
#
# list_result = [3, 8, 1, 5, 8]
# for i in range(len(list_result)):
#     print(list_result[i])

# SOLUTION
# number_list = [int(el) for el in input().split(', ')]
# even_nums = [num for num in range(len(number_list)) if number_list[num] % 2 == 0]
# print(even_nums)
nums_as_string = input().split(', ')
nums = [int(el) for el in nums_as_string]
filtered_nums = [index for index in range(len(nums)) if nums % 2 == 0]
print(filtered_nums)