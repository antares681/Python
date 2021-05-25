word_list = [element for element in input().split() if element == element[::-1]]
palindrome_counter = word_list.count(input())
print(f"{word_list}\nFound palindrome {palindrome_counter} times")