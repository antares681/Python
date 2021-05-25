n = int(input())

counter = 0
symbol = "*"
for i in range (1, n + 1, 1):
    for j in range (0, i):
        print(symbol, end='')
    print()

for i in range (n - 1, 0, -1):
    for j in range (0, i):
        print(symbol, end='')
    print()