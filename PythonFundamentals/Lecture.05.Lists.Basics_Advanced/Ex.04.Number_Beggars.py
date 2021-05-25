#Прочитаме от конзолата сумите за раздаване
sums_list = input().split(", ")
#прочитаме от конзолата броя просяци
number_of_beggars = int(input())
#листа с сумите за всеки просяк
sums_per_beggar = []
#цикъл с итерации колко са броя просяци
start_index = 0
# вложен цикъл

for beggars in range(number_of_beggars):
    current_sum = 0

    for each_sum in range(start_index, len(sums_list), number_of_beggars):
        current_sum += int(sums_list[each_sum])
    sums_per_beggar.append(current_sum)
    start_index += 1
print(sums_per_beggar)





