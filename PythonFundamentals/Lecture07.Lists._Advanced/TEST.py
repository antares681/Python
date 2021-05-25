# #test_list = input().split(" ")
# # test_list = list(map(int, test_list))
# # test_list = test_list[-1] + 1
# # hey = ["lol", "hey","water","pepsi","jam"]
# #
# # for item in hey:
# #     print(item)
# #
# # print(hey)
#
# number = int(input())

# EXAMPLE 1
# class Comment:
#     def __init__(self, username, content, likes = 0):
#         self.username = username
#         self.content = content
#         self.likes = likes
#
# comment = Comment("user", "I like this book")
# print(comment.username)
# print(comment.content)
# print(comment.likes)

#EXAMPLE 2

# class SlidoComment:
#     def __init__(self, autho'' username, comment, likes = 0, dilikes = 0):
#
# numbers_list = input().split(', ')
# x = 0
# for num in numbers_list:
#     print()
#     x += 1

# letter_code = [1, 2, 3, 4, 5, 6]
# letter_code_string = [str(integer) for integer in letter_code]
# print(letter_code_string)
# #
# integers = [1, 2, 3]
# strings = [str(integer) for integer in integers]
#
# a_string = "".join(strings)
# an_integer = int(a_string)
# print(an_integer)

# word = 234234dfd
# letter_code = [(int(i) for i in word if i.isdigit())]
# # letter_code_as_string = [str(i) for i in letter_code]
# # ascii_code = "".join(letter_code_as_string)
# print(letter_code)

# test_list = [5,5,5]
# test_list[1] -=  5
# print(test_list)

# targets_sequence = [int(el) for el in input().split()]
# initial_sequence_length = targets_sequence.copy()
#
# while True:
#     command = input().split()
#     if command[0] == 'End':
#         break
#
#     if command[0] == 'Shoot':
#         if int(command[1]) <= len(targets_sequence):
#             targets_sequence[int(command[1])] -= int(command[2])
#             if targets_sequence[int(command[1])] <= 0:
#                 targets_sequence.pop(int(command[1]))
#
#     elif command[0] == "Add":
#         if int(command[1]) < len(targets_sequence):
#             for el in targets_sequence:
#                 if targets_sequence.index(el) == int(command[1]):
#                     targets_sequence.insert(int(command[1]), int(command[2]))
#         else:
#             print("Invalid placement!")
#
#     elif command[0] == "Strike":
#         target_index = int(command[1])
#         radius = int(command[2])
#         if 0 <= target_index - radius and 1 + radius * 2 <= len(targets_sequence):
#             targets_sequence.remove(targets_sequence[target_index])
#             for targets in range(radius):
#                targets_sequence.remove(targets_sequence[target_index])
#                targets_sequence.remove(targets_sequence[target_index-1])
#
#         else:
#             print('Strike missed!')
#
# target_list = [str(el) for el in targets_sequence]
# print("|".join(target_list))

# #ВАРИАНТ СТРИНГ
#
# second_row = ['2', '2', '2']
# if second_row[0] == second_row[1] == second_row[2] and not "0":
#     res1 = True
# else:
#     res1 = False
# print(f'TEST AS STRINGS: {res1}')
#
# #ВАРИАНТ ИНТЕДЖЕР
# if second_row[0] == second_row[1] == second_row[2] and not 0:
#     row_2 = [int(i) for i in second_row]
#     res2 = True
# else:
#     res2 = False
# print(f'TEST AS INTEGERS: {res2}')

students = ['Peter', 'George', 'Amy']
for student in range (len(students)):
    print(', '.join(students[student]))

# print([', '.join(student) for student in students])