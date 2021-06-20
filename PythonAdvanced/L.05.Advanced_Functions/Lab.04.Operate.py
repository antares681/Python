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

#TODO SOLUTION 3

def operate(operator, *args):
    return reduce(lambda x, y: eval(f'{x} {operator} {y}'), args)

print(operate('+', 1, 2, 3))

#TODO MAPPER EXAMPLE

#possible_operators = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y,} Това как стои ?