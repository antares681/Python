def reverse_Numbers(data):
    reversed_stack = []
    stack = [i for i in data.split(' ')]
    while stack:
        reversed_stack.append(stack.pop())
    return ' '.join(reversed_stack)

print(reverse_Numbers(input()))