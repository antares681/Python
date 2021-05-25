numbers_list = input().split()
numbers_list = [int(i) for i in numbers_list]
numbers_to_remove = int(input())

for nums in range(numbers_to_remove):
    numbers_list.remove(min(numbers_list))

print(numbers_list)
