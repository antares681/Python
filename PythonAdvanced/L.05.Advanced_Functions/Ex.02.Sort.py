# #SOLUTOIN 1
# print(sorted([int(x) for x in input().split()], reverse=False))  #not properly sorted
#
# #SOLUTION 2
# print(sorted(list(map(lambda x: int(x), input().split())), reverse=True))

#SOLUTION 3

data = input().split()
print([int(i) for i in sorted(data, key = lambda x: ord(x[0]))])