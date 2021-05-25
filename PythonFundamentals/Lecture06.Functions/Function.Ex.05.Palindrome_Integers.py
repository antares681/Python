def palindrome_evaluator(element):
    is_palindrome = None
    if element == element[::-1]:
        return True
    return False

list_numbers = input().split(", ")

for element in list_numbers:
    print(palindrome_evaluator(element))
