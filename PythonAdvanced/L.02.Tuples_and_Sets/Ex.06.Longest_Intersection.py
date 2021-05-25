lines_nmbr = int(input())
longest_intersection = set()
for el in range(lines_nmbr):
    first_set, second_set, intersection = set(), set(), set()

    first_range, second_range = input().split('-')
    first_start, first_end = first_range.split(',')
    second_start, second_end = second_range.split(',')
    first_start, first_end, second_start, second_end = int(first_start), int(first_end), int(second_start), int(second_end)

    for el in range(first_start, first_end+1):
        first_set.add(el)
    for el in range(second_start, second_end+1):
        second_set.add(el)
        intersection = first_set & second_set
    if len(intersection) > len(longest_intersection):
        longest_intersection = first_set & second_set

longest_intersection = [str(el) for el in longest_intersection]
print(f'Longest intersection is [{", ".join(longest_intersection)}] with length {len(longest_intersection)}')
