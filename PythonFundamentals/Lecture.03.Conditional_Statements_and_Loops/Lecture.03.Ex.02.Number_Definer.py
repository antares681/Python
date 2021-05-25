num = float(input())

if num == 0:
    print('zero')

if -1000000 > num or num > 1000000:
    print('large', end=" ")
elif -1 < num < 0 or 0 < num < 1:
    print('small', end=" ")

if num > 0:
    print('positive')
elif num < 0:
    print('negative')
