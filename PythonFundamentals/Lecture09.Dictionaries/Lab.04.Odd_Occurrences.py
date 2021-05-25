data = (input().lower()).split()
data_dict = {}
for el in data:
    if el not in data_dict:
        data_dict[el] = 0
    data_dict[el] += 1
print(" ".join([el for el in data_dict if data_dict[el] % 2 != 0]), end = " ")

# words = input().split(" ")
# print(words)
# dictionary ={}
#
# for word in words:
#     word_lower = word.lower()
#     if word_lower not in dictionary:
#         dictionary[word_lower] = 0
#     dictionary[word_lower] += 1
# for (key, value) in dictionary.items():
#     if value % 2 !=0:
#         print(key, end=" ")
