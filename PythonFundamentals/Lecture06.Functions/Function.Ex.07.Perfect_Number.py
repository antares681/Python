def perfect_nmbr_chker(data):
    list_numbers = []

    for element in range(1, data):
        if data % element == 0:
            list_numbers.append(element)

    if sum(list_numbers) == data:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())

print(perfect_nmbr_chker(number))