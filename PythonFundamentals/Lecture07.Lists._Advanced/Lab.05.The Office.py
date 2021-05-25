employees_list = input().split()
multiplayer = int(input())
happy_employees = []
unhappy_employees = []

modified_list = [int(element) * multiplayer for element in employees_list]
avg_happiness = sum(modified_list) / len(modified_list)

for employee_happiness in modified_list:
    if employee_happiness >= avg_happiness:
        happy_employees.append(employee_happiness)
    else:
        unhappy_employees.append(employee_happiness)

if len(happy_employees) >= len(unhappy_employees):
    print(f"Score: {len(happy_employees)}/{len(modified_list)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(modified_list)}. Employees are not happy!")