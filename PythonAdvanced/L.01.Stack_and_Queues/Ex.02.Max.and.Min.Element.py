def queries(elements):
    stack = []
    for i in range(elements):
        command = input().split()
        if int(command[0]) == 1:
            stack.append(int(command[1]))
        elif int(command[0]) == 2:
            if len(stack) > 0:
                stack.pop()
        elif int(command[0]) == 3:
            if len(stack) > 0:
                print(max(stack))
        elif int(command[0]) == 4:
            if len(stack) > 0:
                print(min(stack))
    rev_stack = []
    while stack:
        rev_stack.append(str(stack.pop()))
    if len(rev_stack) > 0:
        return ', '.join(rev_stack)

print(queries(int(input())))