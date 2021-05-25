class Person:
    max_age = 155
    id = 0
    def __init__(self, name, sex, location, seen=False):
        self.name = name
        self.sex = sex
        self.location = location
        Person.id += 1
        self.age = 45
        self.seen = seen
        self.id = Person.id
    def info_person(self):
        return f'{self.name} is a {self.sex} from {self.location} not older than {self.age}\n personal ID is {self.id}'


def check():
    status = True
    for el in range(len(objects_list)):
        if objects_list[el].seen = True


objects_list = []
data_list = [['Pesho', 45, 'Sofia'], ['Vasko', 42, 'Soda']]
for data_set in data_list:
    name, sex, location = data_set[0], data_set[1], data_set[2]
    objects_list.append(Person(name, sex, location))


query = input('Enter query: ')
while not query == 'End':
    for el in range(len(objects_list)):
        print(info_person())
    print('There is no such person in the DataBASE!')
            # print(objects_list[el].name)
            # print(objects_list[el].sex)
            # print(objects_list[el].location)
            # print(objects_list[el].max_age)
    query = input('Enter query: ')

print('Thank you and good bye!')


a = 58.3432423
print(f'{a:.2f}')
print(f'{int(a):02d}')

