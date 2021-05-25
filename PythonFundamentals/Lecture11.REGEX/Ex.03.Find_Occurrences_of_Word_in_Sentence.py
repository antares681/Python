import re
data = input().lower()
regex_el = input().lower()
regex = rf"\b{regex_el}\b"

match = re.findall(regex, data, re.IGNORECASE)
print(len(match))