# #TODO SOLUTION 1 OUT OF TIME LIMIT
#
# from itertools import permutations, chain
# numbers = [n for n in input().split(', ')]
# n = len(numbers)
# permutations = set(permutations(['-'] * n + ['+'] * n , n))
#
# for permutation in permutations:
#
#     exp = (''.join((list(chain(*zip(permutation, numbers))))))
#     res = eval(exp)
#     print(f"{exp} = {res}")
#
#
# #TODO SOLUTION 2 - for JUDGE
#
# from itertools import product
# numbers = input().split(', ')
# n = len(numbers)
# products = [list(x) for x in (product('+-', repeat=n))]
#
# for element in products:
#     zipped = [''.join(x) for x in list(zip(element, numbers))]
#     exp = ''.join(zipped)
#     res = eval(exp)
#     print(f"{exp}={res}")

def expression(nums, current_result = 0):
    if not nums:
        return
    expression(nums[1:], current_result+nums[0])

expression([1, 2, 3])