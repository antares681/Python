try:
    with open('numbers.txt', 'r') as file:
        print(sum([int(el[:-1]) for el in file.readlines()]))

except FileNotFoundError:
    print('File not found')