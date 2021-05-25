employees = 3
employee_per_hour = []
hour_counter = 0
employee_per_hour =[int(input()) for employee in range(3)]
total_visitor_number = int(input())

while total_visitor_number > 0:
    total_questions_per_hour = sum(employee_per_hour)
    hour_counter += 1
    if not hour_counter % 4 ==0:
        if total_visitor_number - total_questions_per_hour > 0:
            total_visitor_number -=total_questions_per_hour
        else:
            break

print(f"Time needed: {hour_counter}h.")
