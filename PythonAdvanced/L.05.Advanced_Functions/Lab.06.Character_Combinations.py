from itertools import permutations

data = [int(x) if x.isdigit() else x for x in input()]
result = permutations(data,len(data))
[print(''.join(x)) for x in list(result)]

#TODO WHY IT CANNOT PRINT ALL 2 PRINTS EITHER FIRST TWO OR THE SECOND
# print(list(result))

from itertools import permutations
data = input()
[print(''.join(x)) for x in list(permutations(data,len(data)))]


