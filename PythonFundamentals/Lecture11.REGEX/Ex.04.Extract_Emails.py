import re

regex = r'(^|(?<=\s))[a-z0-9]+[\._-]?[a-z0-9]+@([a-z]+\-?[a-z]+(\.[a-z]+\-?[a-z]+)+)'
data = input()

for match in re.finditer(regex, data):
    print(match.group())
