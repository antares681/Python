num = int(input())

for i in range(2, num):
        if num % i == 0:
            is_Prime = False
            break

else:
    is_Prime = True

print(is_Prime)
