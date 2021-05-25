nmbr_rows = int(input())
register_list = {}
register_list_avg = {}
for student in range(nmbr_rows):
    name = input()
    grade = float(input())
    if name not in register_list:
        register_list[name] = [grade]
    else:
        register_list[name].append(grade)

students_out = []

for k, v in register_list.items():
    v = sum(v) / len(v)
    if v < 4.50:
        students_out.append(k)
    register_list_avg[k] = float(v)

for student in students_out:
    del register_list_avg[student]

sorted_list_avg = sorted(register_list_avg.items(), key = lambda x:-x[1])

for k, v in sorted_list_avg:
    print(f'{k} -> {v:.2f}')