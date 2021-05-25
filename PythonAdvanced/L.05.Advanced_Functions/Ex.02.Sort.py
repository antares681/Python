#SOLUTOIN 1
print(sorted([int(x) for x in input().split()], reverse=True))

#SOLUTION 2
print(sorted(list(map(lambda x: int(x), input().split())), reverse=True))

