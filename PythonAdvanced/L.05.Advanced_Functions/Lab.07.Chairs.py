from itertools import combinations
names, nmbr_chairs = input().split(', '), int(input())
[print(', '.join(x)) for x in list(combinations(names, nmbr_chairs))]