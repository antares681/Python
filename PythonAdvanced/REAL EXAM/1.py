# 100/100 - SIBINA

from collections import deque

chocolates = [int(el) for el in input().split(', ')]
cups_of_milk = deque([int(el) for el in input().split(', ')])
milkshakes = 0
enough = False

while True:
    if len(chocolates) == 0 or len(cups_of_milk) == 0:
        break
    chocolate = chocolates[-1]
    cup_of_milk = cups_of_milk[0]

    if cup_of_milk <= 0 or chocolate <= 0:
        if cup_of_milk <= 0:
            cups_of_milk.popleft()
        if chocolate <= 0:
            chocolates.pop()
        continue
    if chocolate == cup_of_milk:
        milkshakes += 1
        cups_of_milk.popleft()
        chocolates.pop()

    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5
    if milkshakes == 5:
        enough = True
        break

if enough:
    print('Great! You made all the chocolate milkshakes needed!')
else:
    print('Not enough milkshakes.')
if chocolates:
    print(f'Chocolate: {", ".join([str(el) for el in chocolates])}')
else:
    print('Chocolate: empty')
if cups_of_milk:
    print(f'Milk: {", ".join([str(el) for el in cups_of_milk])}')
else:
    print('Milk: empty')