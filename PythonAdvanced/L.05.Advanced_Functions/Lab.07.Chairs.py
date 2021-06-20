# from itertools import combinations
# names, nmbr_chairs = input().split(', '), int(input())
# [print(', '.join(x)) for x in list(combinations(names, nmbr_chairs))]

#TODO SOLUTION 2
def combinations(names, count, current_names=[]):
    if len(current_names) == count:
        print(', '.join(current_names))
    for i in range(len(names)):
        current_names.append(names[i])
        combinations(names[i+1], count, current_names)
        current_names.pop()

names = input().split(', ')
n = int(input())
combinations(names, n)