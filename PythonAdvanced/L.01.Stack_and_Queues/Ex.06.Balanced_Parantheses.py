# #TEST 75%
#
# def lenght_validator(data):
#     if len(data) % 2 == 0:
#         return True
#     return False
#
# def symbol_validator(data, combinations):
#     for el in data:
#         if el in [x for v in combinations.values() for x in v]:
#             continue
#         else:
#             return False
#     return True
#
# def parentheses_validator(first_half, second_half, combinations):
#     is_valid = True
#     for element in range(len(first_half)):
#         fh, sh = first_half.pop(), second_half.popleft()
#         if not is_valid:
#             break
#         for el in range(len(combinations)):
#             a, b = combinations[el][0], combinations[el][1]
#             if fh == combinations[el][0] and sh == combinations[el][1]:
#                 is_valid = True
#                 break
#             else:
#                 is_valid = False
#     if is_valid:
#         return 'YES'
#     return 'NO'
#
# from collections import deque
# valid_combinations = {0:['{', '}'], 1:['(', ')'], 2:['[', ']']}
#
# data = input()
# half = int(len(data)/2)
# first_half_stack = [element for element in data[:half]]
# second_half_que = deque([element for element in data[half:]])
#
# if data and lenght_validator(data) and symbol_validator(data, valid_combinations):
#     result = parentheses_validator(first_half_stack, second_half_que, valid_combinations)
# else:
#     result = 'NO'
# print(result)

opening = ['{', '[', '(']
closing = ['}',']',')']

def stringAnalyzer(opening, closing):
    data = input()
    parentheses_stack = []
    if not data or not len(data) % 2 == 0:
        return 'NO'
    elif data:
        for el in range(len(data)):
            if data[el] == opening[0] or data[el] == opening[1] or data[el] == opening[2]:
                parentheses_stack += data[el]
            elif parentheses_stack and (data[el] == closing[0] or data[el] == closing[1] or data[el] == closing[2]):
                curr_parantheses = parentheses_stack.pop()
                if not f"{curr_parantheses}{data[el]}" in ['[]','{}','()']:  #EITHER THIS OR BELOW
                    return 'NO'
                # if curr_parantheses == "[" and not data[el] == "]":
                #     return 'NO'
                # elif curr_parantheses == "{" and not data[el] == "}":
                #     return 'NO'
                # elif curr_parantheses == "[" and not data[el] == "]":
                #     return 'NO'
                else:
                    is_valid = True
                    continue
            else:
                return 'NO'

    if not is_valid or parentheses_stack:
        return 'NO'
    return 'YES'

result = stringAnalyzer(opening, closing)
print(result)