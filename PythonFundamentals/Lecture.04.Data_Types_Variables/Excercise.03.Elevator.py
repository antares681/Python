from math import ceil

number_of_persons = int(input())
capacity_of_elevator = int(input())

if number_of_persons % capacity_of_elevator == 0:
    courses = number_of_persons / capacity_of_elevator
else:
    courses = ceil(number_of_persons / capacity_of_elevator)

print(f'{courses:.0f}')