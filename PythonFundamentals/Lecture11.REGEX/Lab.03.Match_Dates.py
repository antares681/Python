import re
test_string = input()
pattern = r'\b(\d{2})(?P<separator>[\/.-])([A-Z][a-z]{2})(?P=separator)(\d{4})\b'
matches = re.findall(pattern, test_string)
print(matches)
for n in range(len(matches)):
    print(f'Day: {matches[int(n)][0]}, Month: {matches[n][2]}, Year: {matches[n][3]}')


#TEST STRING '13/Jul/1928, 10-Nov-1934, , 01/Jan-1951,f 25.Dec.1937 23/09/1973, 1/Feb/2016'
