# my_dict = {}
# word = input()
# for char in word:
#     if not char == " ":
#         if char in my_dict:
#             my_dict[1]+= 1
#         else:
#             my_dict[1] = 1
# for key,value in dictionary.items():
#     print(f'{key} -> {value}')

#MY SOLUTION
data_dict = {}
data = [el for el in input() if not el == " "]
for k in range(len(data)):
    if data[k] in data_dict:
        data_dict[data[k]] +=1
    else:
        data_dict[data[k]] = 1
for k, v in data_dict.items():
    print(f'{k} -> {v}')

