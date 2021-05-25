def contest_sorter(data):
    contenders = {}
    while not data == 'end of contests':
        contest, password = data.split(':')
        if not contest in contenders:
            contenders[contest] = password
        else:
            contenders[contest] = [contenders[contest]]
            contenders[contest].append(password)
        data = input()
    return contenders

def dataSorter():
    data = input()
    while not data == 'end of submission':
        contest, password, username, points = data.split('=>')
        if contest in contenders_list and contenders_list[contest] == password:
            
            return
        else:
            return
        data = input()

contenders_list = contest_sorter(input())
result = dataSorter()
print(result)