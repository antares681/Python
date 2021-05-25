def odd_and_even_summary (number):
    list_odds = []
    list_even = []

    for i in number:
        if int(i) % 2 == 0:
            list_even.append(i)
        else:
            list_odds.append(i)

    sum_even = 0
    for i in list_even:
        sum_even +=int(i)

    sum_odds = 0
    for i in list_odds:
        sum_odds +=int(i)

    return sum_odds, sum_even

num = input()

sum_odds, sum_even = odd_and_even_summary(num)

print(f'Odd sum = {sum_odds}, Even sum = {sum_even}')
