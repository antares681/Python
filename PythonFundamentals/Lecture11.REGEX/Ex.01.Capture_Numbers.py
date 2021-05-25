import re
pattern = re.compile(r'\d+')
matches = []
data = input()

while data:
    current = pattern.findall(data)
    if current:
        matches.extend(current)
    data= input()
print(' '.join(matches))

# print([c for c in range(12)])
