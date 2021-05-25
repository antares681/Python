# TODO SOLUTION 1
# import re
# pattern = re.compile(r'\||\d')
# data = input()
# matches = "".join([i for i in data if i in pattern.findall(data)])
# data = ''.join(matches.split('|')[::-1])
# print(" ".join([el for el in data]))
#
#
#TODO SOLUTION 2
# import re
# pattern = re.compile(r'\||\d+\{?}\s')
# data = input()
# matches = "".join([i for i in data if i in pattern.findall(data)])
# print(" ".join([el for el in ''.join(matches.split('|')[::-1])]))


# # #TODO SOLUTION 3
# #
# print(" ".join([el for el in ''.join(("".join([el for el in input() if not el == " "])).split('|')[::-1])]))

# #TODO SOLUTION 4  - 100%
#
data = [el.split() for el in [str(i) for i in (input().split('|')[::-1])]]
d = " ".join([" ".join(el) for el in data if not el == []])
print(d)

## TODO SOLUTION 5 - 100%
#
# print(" ".join([" ".join(el) for el in [el.split() for el in [str(i) for i in (input().split('|')[::-1])]] if not el == []]))
# # -3 1| 4 5 6 7  |  8 99