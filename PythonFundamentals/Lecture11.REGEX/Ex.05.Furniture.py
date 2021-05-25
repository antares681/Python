#r'>>([A-Za-z]+)<<(\d+[\.]?\d+?)!(\d+\b)'

# import re
#
# pattern = r'(?<=>>)(?P<name>[A-Za-z]+)<<(\d+\.?\d+?)\!(\d+)\b'
# product ={}
# filtered_list =[]
# command = input()
#
# while not command == 'Purchase':
#     for match in re.finditer(pattern, command):
#         filtered_list = list(match.groups())
#     product[filtered_list[0]] = filtered_list[1:]
#     command = input()
#
# expences = []
# print('Bought furniture:')
# if product:
#     for k,v in product.items():
#         expences.append(float(v[0])*int(v[1]))
#         print(k)
#     print(f'Total money spend: {sum(expences)}')
# else:
#     print(f'Total money spend:')

import re

pattern = re.compile(r'>>(?P<name>[A-Za-z]+)<<(?P<price>\d+\.?\d+?)\!(?P<quantity>\d+)')
                #>>(?P<name>[a-zA-Z]+)<<(?P<price>\d+\.?\d+?)\!(?P<quantity>\d+)

command = input()
furniture_bought = []
total_money = 0

while not command == 'Purchase':
    match = pattern.match(command)
    if match:
        data = match.groupdict()
        furniture_bought.append(data['name'])
        total_money += int(data['quantity']) * float(data['price'])
    command = input()

print('Bought furniture:')
if furniture_bought:
    print('\n'.join(furniture_bought))
print(f'Total money spend: {total_money:.2f}')