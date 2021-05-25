# def subexpressionGet(expression):
#     expression = [i for i in expression]
#     stack = []
#     result = []
#     for current_idx in range(len(expression)):
#         if expression[current_idx] == '(':
#             stack.append(current_idx)
#         elif expression[current_idx] == ')':
#             start_idx = int(expression.pop())
#             result.append(expression[start_idx:current_idx+1])
#     return result
#
# print(subexpressionGet('1+(2-(2+3)*4 / (3+1))*5'))

# def get_subexpression(expression):
#     stack=[]
#     result=[]
#     for index in range(len(expression)):
#         if expression[index] == '(':
#             stack.append(index)
#         elif expression[index] == ')':
#             start_idx = stack.pop()
#             result.append(expression[start_idx:index])
#     return result
# print(get_subexpression('1+(2-(2+3)*4 / (3+1))*5'))

def getSubexpression():
    expression = input()
    cash_stack = []
    result = []

    for curr_idx in range(len(expression)):
        if expression[curr_idx] == "(":
            cash_stack.append(curr_idx)
        elif expression[curr_idx] == ")":
            start_idx = cash_stack.pop()
            result.append(expression[start_idx:curr_idx+1])
    return result

[print(i) for i in getSubexpression()]