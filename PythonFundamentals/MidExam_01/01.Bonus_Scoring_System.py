from math import ceil

count_of_students = int(input())
count_of_lectures = int(input())
course_bonus = int(input())
student_results = []
student_attendances = 0
student_attendances_register = []

if not count_of_lectures <= 0:

    while count_of_students > 0:
        student_attendances = int(input())
        student_results.append(student_attendances/count_of_lectures * (5 + course_bonus))
        student_attendances_register.append(student_attendances)
        count_of_students -=1

    max_student_result = max(student_results)
    max_student_attendances = student_attendances_register[student_results.index(max_student_result)]
    print(f"Max Bonus: {ceil(max_student_result):.0f}.")
    print(f"The student has attended {max_student_attendances:.0f} lectures.")

else:
    print(f"Max Bonus: {0}.")
    print(f"The student has attended {0} lectures.")