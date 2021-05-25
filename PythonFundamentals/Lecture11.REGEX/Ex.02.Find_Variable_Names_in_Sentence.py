import re
data = input()
pattern = r'\(^_|(?<=\s)[A-Za-z0-9]+\b'
matches = re.findall(pattern, data)
list_to_print = []
for el in range(len(matches)):
    list_to_print.append(matches[el][1:])
print(','.join(list_to_print))
