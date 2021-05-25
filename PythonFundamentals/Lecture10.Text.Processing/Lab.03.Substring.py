data_1 = input()
data_2 = input()

while data_1 in data_2:
    data_2 = data_2.replace(data_1, '')
print(data_2)