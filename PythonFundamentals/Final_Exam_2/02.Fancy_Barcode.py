import re
pattern = re.compile(r'@#+([A-Z])([A-Za-z0-9]+){4}([A-Z])@#+')
nmbr_lines = int(input())
dig_match = []

for i in range(0, nmbr_lines):
    text = input()
    match = pattern.match(text)
    if match:
        dig_match = ''.join([i for i in ''.join(match.group()) if i.isdigit()])
        if dig_match:
            print(f'Product group: {dig_match}')
        else:
            print(f'Product group: 00')
    else:
        print('Invalid barcode')



''''
6
@###Val1d1teM@###
@#ValidIteM@#
##InvaliDiteM##
@InvalidIteM@
@#Invalid_IteM@#
@#ValiditeM@#
'''