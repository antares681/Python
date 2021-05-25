# def GradeComplier(nmbr):
#     note_records = {}
#     for i in range(nmbr):
#         name, grade = input().split(' ')
#         if not name in note_records:
#             note_records[name] = [float(grade)]
#         else:
#             note_records[name].append(float(grade))
#
#     return note_records
#
# def avg(item):
#     return sum(item)/len(item)
#
# to_print = GradeComplier(int(input()))
#
# for k, v in to_print.items():
#
#     grades = ["{:.2f}".format(el) for el in v]
#     print(f'{k} -> {" ".join(map(str,grades))} (avg: {avg(v):.2f})')

    # print(f'{k} -> {str(v)[1:-1]} (avg: {avg(v):.2f})')
    # "{:.2f}".format(5)

#TODO SOLUTION 2
from collections import defaultdict

def GradeComplier(nmbr):
    note_records = defaultdict(list)
    for _ in range(nmbr):
        name, grade = input().split(' ')
        note_records[name].append(float(grade))
    return note_records

def avg(item):
    return sum(item)/len(item)

to_print = GradeComplier(int(input()))

for k, v in to_print.items():
    grades = ["{:.2f}".format(el) for el in v]
    print(f'{k} -> {" ".join(map(str,grades))} (avg: {avg(v):.2f})')