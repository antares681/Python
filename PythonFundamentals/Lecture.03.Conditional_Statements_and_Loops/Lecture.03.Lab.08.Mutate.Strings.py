# string_1 = input()
# string_2 = input()
# current_result = ""
# previous_result = string_1
#
# for index in range(len(string_1)):
#     for i in range(index+1):
#         current_result += string_2[i]
#     for j in range(index+1, len(string_2)):
#         current_result += string_1[j]
#     if current_result != previous_result:
#         previous_result = current_result
#         print(current_result)
#         current_result = ""
#     else:
#         current_result = ""

string_1 = input()
string_2 = input()
index = 0
for i in string_1:
    if i != string_2[index]:
        string_1 = string_1.replace(i, string_2[index], 1)
        print(string_1)
    index += 1
