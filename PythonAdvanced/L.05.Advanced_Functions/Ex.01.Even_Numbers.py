##TODO SOLUTION 1
# [print(el) for el in [int(x) for x in input().split()] if el % 2 == 0]

##TODO SOLUTION 2
print(list(int(x) for x in (filter(lambda x: int(x) % 2 == 0, input().split()))))