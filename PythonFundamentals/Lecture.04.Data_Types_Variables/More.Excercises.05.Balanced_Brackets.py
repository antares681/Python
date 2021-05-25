lines_number = int(input())
opening_brackets_counter = 0
closing_brackets_counter = 0
symbols_list = []
previous_element = ''

for elements in range(lines_number):
    symbol = input()
    symbols_list.append(symbol)

for element in range(len(symbols_list)):

    if symbols_list[element] == '(':
        if previous_element == symbols_list[element]:
            break
        previous_element = symbols_list[element]
        opening_brackets_counter +=1

    if symbols_list[element] == ')':
        if previous_element == symbols_list[element]:
            break
        previous_element = symbols_list[element]
        closing_brackets_counter += 1

if opening_brackets_counter == closing_brackets_counter:
    print('BALANCED')
else:
    print('UNBALANCED')


# previous_bracket = ""
# result = ""
#
# lines_number = int(input())
#
# if lines_number == 0:
#     result = "UNBALANCED"
# elif lines_number == 1 or lines_number < 0:
#     result = "UNBALANCED"
#     symbol = input()
# else:
#     for i in range(0, lines_number):
#
#         symbol = input()
#
#         if symbol == ")" and previous_bracket == "(":
#             result = "BALANCED"
#             previous_bracket = ")"
#         elif symbol == "(":
#             previous_bracket = "("
#             result = "BALANCED"
#         else:
#             if not symbol =="(" and not symbol == ")" and not result == "UNBALANCED" :
#                 result = "BALANCED"
#                 continue
#             else:
#                 result = "UNBALANCED"
#
# print(result)

#     symbol = input()
#
#     if symbol == "(":
#         counter_opening_brackets += 1
#         counter_conseq_opening_brackets+=1
#         if counter_closing_brackets > counter_opening_brackets:
#             result = "UNBALANCED"
#             break
#
#     if symbol == ")":
#         counter_closing_brackets += 1
#         if counter_closing_brackets - counter_opening_brackets >= 2:
#             result = "UNBALANCED"
#             break
#
#     if counter_opening_brackets == counter_closing_brackets and not counter_opening_brackets == 0 == counter_closing_brackets:
#         result = "BALANCED"
#     else:
#         result = "UNBALANCED"
#
# print(result)