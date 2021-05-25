# SOLUTION 1 WITH TUPLE
# from collections import defaultdict
#
# dic_factory = defaultdict(int)
# numbers = [float(i) for i in input().split()]
#
# for number in numbers:
#     dic_factory[number] +=1  #countes key or creates such if not avail and counts if such not avail.
#
# [print(f'{k} - {v} times') for k,v in dic_factory.items()]

#SOLUTION 2 WITH SET

numbers = tuple(float(nmbr) for nmbr in input().split())
data_set = set()

for num in numbers:
    if num not in data_set:
        data_set.add(num)
        print(f'{num} - {numbers.count(num)} times')