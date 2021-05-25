lines_number = int(input())
number_list = []
odd = []
even = []
negative = []
positive = []

for i in range (lines_number):
    number_list.append(int(input()))
    if number_list[i] % 2 == 0:
        even.append(number_list[i])
    else:
        odd.append(number_list[i])

    if number_list[i] >= 0:
        positive.append(number_list[i])
    else:
        negative.append(number_list[i])

command = input()

if command == "even":
    print(even)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)
elif command == "odd":
    print(odd)