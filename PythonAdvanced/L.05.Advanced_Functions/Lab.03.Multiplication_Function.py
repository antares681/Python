#TODO SOLUTION1
#from functools import reduce
# multiply = lambda *args: reduce(lambda  a, b: a * b, args)
# print(multiply(1, 2, 3, 4, 5))

# #TODO SOLUTION2
# from functools import reduce
# def multiply(*args):
#     return(reduce(lambda a, b: a * b, args))
#
# print(multiply(1, 2, 3, 4, 5))

# #TODO SOLUTION 3
# from functools import reduce
# from operator import mul
#
# def multiply(*args):
#     return reduce(mul, args)
# print(multiply(1, 2, 3, 4, 5))

# #TODO SOLUTION 4
# from math import prod
# multiply = lambda *args: prod(args)
#
# print(multiply(1, 2, 3, 4, 5))