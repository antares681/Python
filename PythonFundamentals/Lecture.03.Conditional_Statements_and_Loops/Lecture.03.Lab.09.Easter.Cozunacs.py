budget = float(input())
price_flower = float(input())
price_eggs = price_flower * 0.75
price_milk = price_flower * 1.25
price_cozonac = price_milk * 0.25 + price_eggs + price_flower
price_cozonac_no_milk = price_milk * 0.25 + price_eggs + price_flower
dyed_eggs_counter = 0 # on every third cozonac lose eggs in amount cosonac_counter - 2
cozonacs_counter = 0
milk_counter = 0

while True:
    if milk_counter == 0:
        expenditure = price_cozonac
        milk_counter += 1
    else:
        expenditure = price_cozonac_no_milk
        milk_counter -= 0.25

    if budget >= expenditure:
        budget -= expenditure
        dyed_eggs_counter += 3
        cozonacs_counter += 1
        if cozonacs_counter % 3 == 0:
            dyed_eggs_counter -= cozonacs_counter - 2
    else:
       break

print(f"You made {cozonacs_counter} cozonacs! Now you have {dyed_eggs_counter} eggs and {budget:.2f}BGN left.")




