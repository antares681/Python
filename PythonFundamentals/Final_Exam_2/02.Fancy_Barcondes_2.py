import re
pattern = re.compile(r'@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+')
nmbr_lines = int(input())
digits = '00'
for lines in range (nmbr_lines):
    data = input()
    match = pattern.match(data)
    if match:
        digits = ''.join([el for el in match.group() if el.isdigit()])
        if digits:
            print(f'Product group: {digits}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
