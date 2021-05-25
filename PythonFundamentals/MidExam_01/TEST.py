# # the_list = input().split(" ")
# # step = int(input())
# # step -= 1
# # idx = step
# # new_list = []
#
# # while not len(the_list) == 1:
# #     new_list.append(the_list.pop(idx))
# #     idx = (idx + step) % len(the_list)
# #     # print(f'Idx{idx}')
# #     # print(f'Step{step}')
# # new_list.append(the_list[0])
# #
#
# # soldiers_list = input().split(" ")
# # position_step = int(input())
# # result = []
# # position = 0
# #
# # while len(soldiers_list) > 0:
# #     position -= 1
# #     position = (position + position_step) % len(soldiers_list)
# #     result.append(soldiers_list.pop(position))
# # print(f"[{','.join(result)}]")
#
# #
# #
# # print(result)
#
# targets_sequence = [int(el) for el in input().split()]
# command = input()
# while command != "End":
#     command = command.split()
#     if command[0] == 'Shoot':
#         if 0 <= int(command[1]) < len(targets_sequence):
#             targets_sequence[int(command[1])] -= int(command[2])
#             if targets_sequence[int(command[1])] <= 0:
#                 targets_sequence.pop(int(command[1]))
#
#     elif command[0] == 'Add':
#         if 0 <= int(command[1]) < len(targets_sequence):
#             target_index = int(command[1])
#             target_value = int(command[2])
#             targets_sequence.insert(target_index, target_value)
#         else:
#             print('Invalid placement!')
#
#     elif command[0] == "Strike":
#         target_index = int(command[1])
#         radius = int(command[2])
#         if 0 <= target_index - radius and target_index + radius < len(targets_sequence):
#             del targets_sequence[target_index - radius:target_index + radius + 1]
#         else:
#             print('Strike missed!')
#     command = input()
# target_list = [str(el) for el in targets_sequence]
# print("|".join(target_list))


count_of_students = int(input())
lectures_count = int(input())
initial_bonus = int(input())

students_list = []
for student in range(count_of_students):
    st_attendance = int(input())
    students_list.append(st_attendance)
    studentAttendance = max(students_list)
    maxBonusPoint = round(studentAttendance / lectures_count * (5 + initial_bonus))
print(f"Max Bonus: {maxBonusPoint}.")
print(f"The student has attended {studentAttendance} lectures.")