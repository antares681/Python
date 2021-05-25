import re

pattern = re.compile(r'([*|@])(?P<key>[A-Z][a-z]{2,})\1\:\s(?P<message>((\[[A-Za-z0-9]\]\|){3})$)')

nmbr_lines = int(input())
for lines in range(nmbr_lines):
    data_string = input()
    match = pattern.search(data_string)
    if match:
        data= match.groupdict()
        ascii = " ".join([str(ord(i)) for i in data['message'] if i.isalpha()])
        print(f'{data["key"]}: {ascii}')
    else:
        print('Valid message not found!')