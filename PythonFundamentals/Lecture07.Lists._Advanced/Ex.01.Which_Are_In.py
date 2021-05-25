# list1 = input().split(', ')
# list2 = input().split(', ')
# list_results = []
#
# for i in list1:
#     for el in list2:
#         if i in el:
#             list_results.append(i)
#
# print(sorted(set(list_results), key = list_results.index))

list1 = input().split(', ')
list2 = input().split(', ')
list_results = [i for i in list1 for el in list2 if i in el]

print(sorted(set(list_results), key = list_results.index))