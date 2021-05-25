courses = {}
command = input()

while not command == 'end':
    command = command.split(' : ')
    course_name = command[0]
    student_name = command[1]

    if course_name not in courses:
        courses[course_name] =[student_name]
    else:
        courses[course_name].append(student_name)

    command = input()

sorted_courses = dict(sorted(courses.items(), key=lambda x: (len(x[1])), reverse=True))
for k, v in sorted_courses.items():
    print(f'{k}: {len(v)}')
    v.sort()
    value = '\n-- '.join(v)
    print(f"-- {value}")