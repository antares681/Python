age = int(input())
drink_type = " "

if age <= 14: #kid
    drink_type = "toddy"
elif 14 < age <= 18: #teen
    drink_type = "coke"
elif 18 < age <= 21: #young adults
    drink_type = "beer"
elif 21 < age:   #adults
    drink_type = "whisky"

print (f'drink {drink_type}')