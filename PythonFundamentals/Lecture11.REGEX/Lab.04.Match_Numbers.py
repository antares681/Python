import re
test_string = input()
pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
matches = re.finditer(pattern, test_string)
for match in matches:
    print(match.group(0), end=' ')

print(matches)

#1 -1 1s 123 s-s -123 _55_ _f 123.456 -123.456 s-1.1 s2 -1- zs-2 s-3.5