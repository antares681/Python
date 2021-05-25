number_list = [int(elements) for elements in input().split(', ')]
control_list = number_list.copy()

group = 10
nums_group = []

while len(control_list) > 0:
    for num in number_list:
        if (group - 10) < num <= group:
            nums_group.append(num)
            control_list.remove(num)
    print(f"Group of {group}'s: {nums_group}")
    group += 10
    nums_group = []