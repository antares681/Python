from collections import deque
name = deque()

command = input()
while not command == 'End':
    if command == 'Paid':
        while name:
           print(name.popleft())
    else:
        name.append(command)
    command = input()
print(f'{len(name)} people remaining.')