from functools import reduce

def operate(operator, *args):
  if operator == '+':
      return reduce(lambda a, b: a + b, args)
  if operator == '-':
      return reduce(lambda a, b: a - b, args)
  if operator == '/':
      return reduce(lambda a, b: a / b, args)
  if operator == '*':
      return reduce(lambda a, b: a * b, args)

print(operate('+', *[1,2,3,4,5,6]))
print(operate('+', 1,2,3,4,5,6))

from functools import reduce

#TODO SOLUTION 2

def operate(operator, *args):
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '/': lambda a, b: a / b,
        '*': lambda a, b: a * b
    }
    return reduce(ops[operator], args)
print(operate('+',*[i for i in range(100_000)]))