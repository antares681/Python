from math import floor
names_nmbr = int(input())

odd_set = set()
even_set = set()

for i in range(names_nmbr):
    name = input()
    name_value = 0
    row_nmbr = i + 1

    for el in name:
        name_value += ord(el)
    name_value = floor(name_value / row_nmbr)

    if name_value % 2 == 0:
        even_set.add(name_value)
    else:
        odd_set.add(name_value)

if sum(even_set) == sum(odd_set):
    result  = even_set + odd_set
elif sum(even_set) < sum(odd_set):
    result = odd_set - even_set
elif sum(even_set) > sum(odd_set):
    result = even_set ^ odd_set

result = ", ".join([str(el) for el in result])
print(result)


#TODO НЕ Е ПОСОЧЕНО, ЧЕ ПРИ ДЕЛЕНИЕТО ДРОБНИТЕ ЧИСЛА СЛЕДВА ДА БЪДАТ ЗАКРЪГЛЕНИЕ С FLOOR