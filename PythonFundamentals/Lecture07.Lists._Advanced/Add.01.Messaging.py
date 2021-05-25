# nums = input().split(" ")
# text = input()
# text_as_list =[]
# final_text = []
#
# for char in text:
#      text_as_list.append(char)
#
# for element in nums:
#     symbol = sum(list(map(int, element)))
#     symbol_to_remove = (symbol % len(text))
#     final_text.append(text_as_list.pop(symbol_to_remove))
#
# print("".join(final_text))


nums = input().split(" ")
text = input()
final_text = []


text_as_list = [char for char in text]

for element in nums:
    symbol = sum(list(map(int, element)))
    symbol_to_remove = (symbol % len(text))
    final_text.append(text_as_list.pop(symbol_to_remove))

print("".join(final_text))
