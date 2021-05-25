#ARGS KWARG

# def sum_func(arg, *args):
#     return arg + sum(args)
#
# print(sum_func(5))
#
# map()


# # TODO REDUCE FUNCTION HOW IT WORKS
# from functools import reduce
#
# def add(a, b):
#     print(f'a = {a}')
#     print(f'b = {b}')
#     return a + b
#
# res = reduce(add, [1, 2, 3, 4, 5, 6])
# print(f'res = {res}')

# #TODO UNPACKING LISTS
#
# def print_nums(*args):
#     return print(args)
#
# nums = [1, 2, 3, 4, 5]
# print_nums(*nums)


# #TODO UNPACKING DICTIONARY
#
# def some_func(name, age):
#     print(f'{name} is {age} years old')
#
# person = {'age': 20, 'name': 'Peter'}
# some_func(**person)


#TODO RECURSIVE FCUNTIONS

def fact(n):
    if n == 1:           #bottom of the stack / BASE CASE
        return(n)      #returns once botton is reached starting from bottom
    return n * fact(n-1)   #going down the stack until the bottom

print(fact(int((input()))))

#EXAMPLE
    #
    # fact(5)                         - > 5 * 24 = 120 - > return 120
    #     4 * fact(3)                 - > 4 * 6 = 24
    #         3 * fact(2)             - > 3 * 2 = 6
    #             2 * fact(1)         - > 2 * 1 = 2
    #                 1* fact(1)      - > 1 * 1 = 1
    #                      fact(1)    - > 1   Bottom reached!!!!(RECURSION UP THE STACK STARTS HERE)

# ALTERNATIVE from itertools combinations / permutations
