command = input()
numbers = list(map(lambda x: int(x), input().split()))
nmbrs_length = len(numbers)

if command == 'Odd':
    print(sum(list(filter(lambda x: x % 2 != 0, numbers))*nmbrs_length))
elif command == 'Even':
    print(sum(list(filter(lambda x: x % 2 == 0, numbers))*nmbrs_length))