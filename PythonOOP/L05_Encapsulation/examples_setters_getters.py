#To access and change the variables, accessor(getter) and mutators(setter) methods should be used as they are part of the class hierarchy
class User:
    def __init__(self, name=str, is_admin=bool):
        self.name = name
        self.is_admin = is_admin

class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.__age = age

    def info(self, user):
        if user.is_admin:
            return self.__age
        return f'{user.name} not allowed. Admin rights needed!'
        # print(self.name)
        # print(self.__age)

    def get_age(self, user):          #getter
        print(self.__age)


    def set_age(self, age):     #setter
        self.age = age

super_admin = User('Admin', True)
user = User('Common User', False)
person = Person('Lazar', 40)
print(person.info(super_admin))
print(person.info(user))
