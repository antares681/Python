lines_nmbr = input()
sum = 0

for i in range(0, int(lines_nmbr)):
    symbol = input()
    symbol_unicode = ord(symbol)
    sum += int(symbol_unicode)

print(f'The sum equals: {sum:.0f}')