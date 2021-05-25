my_dict = {}
resource = input()
while not resource == 'stop':
    resources_qty = int(input())
    if resource not in my_dict:
        my_dict[resource] = resources_qty
    else:
        my_dict[resource] += resources_qty
    resource = input()
for k,v in my_dict.items():
    print(f'{k} -> {v}')