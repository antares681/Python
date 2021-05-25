nmbrs = list(map(int, input().split(', ')))
positive, negative, odd, even = [str(el) for el in nmbrs if el >= 0], [str(el) for el in nmbrs if el < 0], [str(el) for el in nmbrs if not el % 2 == 0], [str(el) for el in nmbrs if el % 2 == 0]
print(f'Positive: {", ".join([el for el in positive])}')
print(f'Negative: {", ".join([el for el in negative])}')
print(f'Even: {", ".join([el for el in even])}')
print(f'Odd: {", ".join([el for el in odd])}')
