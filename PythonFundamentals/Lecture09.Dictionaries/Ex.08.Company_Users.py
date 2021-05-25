data = input()
database = {}
while not data == 'End':
    data = data.split(' -> ')
    company = data[0]
    usr_id = data[1]
    if company in database and usr_id not in database[company]:
        database[company].append(usr_id)
    elif company in database and usr_id in database[company]:
        pass
    else:
        database[company] = [usr_id]
    data = input()

database = sorted(database.items(), key=lambda x: x[0])

for k, v in database:
    print(f'{k}')
    value = '\n-- '.join(v)
    print(f"-- {value}")