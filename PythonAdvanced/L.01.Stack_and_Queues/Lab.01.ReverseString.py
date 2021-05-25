# def reverse_string(text):
#     stack=[]
#     for letter in text:
#         stack.append(letter)
#
#     reversed_stack = []
#     while stack:
#         letter = stack.pop()
#         reversed_stack.append(letter)
#     result = ''.join(reversed_stack)
#     return result
# print(reverse_string('I love Python'))
#

def rev_string(text):
    stack = text[::-1]
    return stack
print(rev_string(input()))
