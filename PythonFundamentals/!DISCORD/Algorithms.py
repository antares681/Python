# #DICTIONARY  COMPREHENSIONS
#
# "bread' 3 'water' 5 'candy' 4"
# data = "bread 3 water 5 candy 4".split(" ")[::-1]
# dect = {data[k+1]: data[k] for k in range(0,len(data)-1,2)}
#
# print(dect)
#
#
# #Solution 1
# Find duplicate number in integer list:
#
#
# def find_duplicates(elements):
#     duplicates, seen = set(), set()
# for element in elements:
#     if element in seen:
#         duplicates.add(element)
#         seen.add(element)
# return list(duplicates)
#
#
# #Solution 2
#
# ll = [1,1,1,2,3,4,4,4,5,6,6,6,6,7,8,9]
# dect = {el:0 for el in ll}
# for el in ll:
#     dect[el] += 1
# print([el for el in dect if dect[el] >= 2])

second_result = [f'even{num}' if num % 2 ==0 else f'odd {num}' for num in range(1,20)]