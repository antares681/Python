saved_money = float(input())
months = int(input())
budget = saved_money * 1
revenue_per_month = budget * 0.25
saved_money = 0

for month in range(1, months+1):
    if not month % 2 == 0:
        saved_money -= saved_money * 0.16
    if month % 4 == 0:
        saved_money += saved_money * 0.25
    saved_money += revenue_per_month

difference = abs(saved_money - budget)

if budget > saved_money:
    print(f'Sorry. You need {difference:.2f}lv. more.')
else:
    print(f'Bravo! You can go to Disneyland and you will have {difference:.2f}lv. for souvenirs.')