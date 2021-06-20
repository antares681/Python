def say_smth(times):
    if times == 0:
        return
    print('I am saying')
    say_smth(times-1)

say_smth(5)
#
#
# def fact(n):
#     if n == 1:
#         return 1
#     return n* fact(n-1)