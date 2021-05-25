data_string = input()
characters = ''
digits = ''
other = ''

for i in data_string:
    if i.isalpha():
        characters += str(i)
    elif i.isdigit():
        digits += i
    else:
        other += i

print(f'{digits}\n{characters}\n{other}')