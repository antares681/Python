# def palindrome(data, idx=0, end_idx = -1):
#     if idx == len(data) // 2:
#         return f"{data} is a palindrome"
#     if data[idx] == data[-1]:
#         return palindrome(data, idx + 1, end_idx - 1)
#     else:
#         return f'{data} is not a palindrome'
#
# print(palindrome("abcba", 0))
# print(palindrome("peter", 0))

def palindrome(data, idx=0, right_index=-1):
    if idx == len(data) // 2:
        return f"{data} is a palindrome"
    if data[idx] == data[right_index]:
        return palindrome(data, idx + 1, right_index - 1)
    else:
        return f'{data} is not a palindrome'