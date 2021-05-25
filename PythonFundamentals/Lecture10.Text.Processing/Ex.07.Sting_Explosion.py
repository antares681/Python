# data = input().split(">")
# explode = 0
# after_explode = []
# for el in data:
#     if el[0].isdigit():
#         explode += int(el[0])
#         if len(el) <= explode:
#             explode -= len(el)
#             el = ">"
#         else:
#             el = ">" + "".join(list(el[explode::]))
#             explode = 0
#     after_explode.append(el)
# print("".join(after_explode))

data = input()
string_to_print = ''
explosion_range = 0
for index in range(len(data)):
    if data[index] == '>':
        explosion_range += int(data[index + 1])
        string_to_print += data[index]
    elif not explosion_range == 0:
        explosion_range -= 1
    else:
        string_to_print += data[index]
print(string_to_print)