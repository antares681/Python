# #1
# A = [[0, 1], [2, 3]]
# flatten_list = []
#
# for subl in A:
#     for item in subl:
#         flatten_list.append(item)
# print(flatten_list)
#
#
# #2
# A = [[0, 1], [2, 3]]
# flatten_list = [item for subl in A for item in subl]
# print(flatten_list)
#
# #3
# from iteration_utilities import deepflatten
#
# multi_depth_list = [[0, 1], [[5]], [6, 4]]
# flatten_list = list(deepflatten(multi_depth_list))
# print(flatten_list)
#
#
# #4 - RECURSION
#
# def flatten(l1)
#     if len(l1) == 1:
#         if type(l1[0]) == list:
#             result = flatten(l1[0])
#     else:
#         result = l1
#
# # recursive case
#     elif type(l1[0]) == list:
#         result = flatten(l1[0]) + flatten(l1[1:])
#     else:
#         result = (l1[0]) + flatten(l1[1:])
#     return result
#
#
# list1 = [[0, 1], [[5]], [6, 7]]
# flatten(list1)
#
#
# #5
# import itertools
#
# List_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # List to be flattened
# List_flat = list(itertools.chain(*List_1))
# print(List_flat)