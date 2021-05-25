# class Person:
#     def __init__(self, name, age):  #__init__ called also construnctro
#         self.name = name
#         self.age = age
#
#     # __call__ , __new__ other two magic method that will be called before __init__
#
#     def get_older(self):
#         self.age += 1
#
#     def __str__(self):  # __str__ = str() - turns the object to string
#         return f'{self.name}; {self.age}'
#
#     def __add__(self, other_person):
#         return Person(self.name + other_person.name, self.age + other_person.age)
#
# pesho = Person('Pesho', 15)
# alex = Person('Alex', 18)
# print(pesho)
# print(alex)
# pesho.get_older()
# alex.get_older()
# print(pesho)
# print(alex)
#
# print(pesho + alex) # will not work without implementation of __add__ method as shown above
# print(f'{pesho} {alex}')


a = {}
a['Aba'] = ['baba', 'dodo']
if not 'baba' in a['Aba']:
    a['Aba'].append(['baba', 'gogo'])
a['Aba']=(['buba', 'gugo'])
print(a)