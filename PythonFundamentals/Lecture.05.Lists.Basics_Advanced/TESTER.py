# def Lazar():
#     print(f'Hello World! Have a great {value}')
# def summary(a, b):
#     return(a + b)
#
# value = input()
# Lazar()
#
# a= int(input())
# b= int(input())
#
# x = summary(a, b)
#
# row = 1000
#
# for i in range (row):
#     print(x * 100, end= " ")
#     x += 50
#

def load_bar_and_print(n):
    bar ['.','.','.','.','.','.','.','.','.','.',]

    if n == 0:
        return bar

    n //= 10

    for num in range(n):
        bar[index] = "%"
    return bar

number = int(input())
bar_result = load_bar(number)