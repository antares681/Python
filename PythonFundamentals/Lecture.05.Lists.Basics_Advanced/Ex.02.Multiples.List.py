factor = int(input())
count = int(input())
result_list = []

while 0 < count:
    result_list.append(factor * count)
    count -= 1

result_list.reverse()
print(result_list)