from math import floor
party_size = int(input())
adventure_days = int(input())
companions_count = party_size

earnings = 0
spendings = 0

for i in range(1, adventure_days + 1):

#Companions calculations
    if i % 10 == 0:
        companions_count -= 2

    if i % 15 == 0:
        companions_count += 5

    earnings += 50
    spendings += 2 * companions_count

#Coins calculations
    if i % 5 == 0:
        earnings += 20 * companions_count

    if i % 3 == 0:
        spendings += 3 * companions_count

    if i % 3 == 0 and i % 5 == 0:
        spendings += 2 * companions_count

    coins = floor((earnings - spendings)/companions_count)

print(f"{companions_count} companions received {coins} coins each.")