class Employee:
    name = 'Harsh'
    salary = '25000'

    def show(self):
        print(self.name)
        print(self.salary)

employee = Employee()
print(getattr(employee, 'name'))   # Harsh
print(hasattr(employee, 'name'))   # True
setattr(employee, 'height', 152)
print(getattr(employee, 'height')) # 152
delattr(Employee, 'salary')


#TODO ONE BY ONE EXAMPLE
#delattr
class Phone:
    def __delattr__(self, attr):
        del self.__dict__[attr]
        print(f"'{str(attr)}' was deleted")

phone = Phone()
phone.color = 'black'
del phone.color  # 'color' was deleted


#__setattr__
class Phone:
    def __setattr__(self, attr, value):
        self.__dict__[attr] = value.upper()

phone = Phone()
phone.color = 'black'
print(phone.color)  # BLACK


#__hasattr__

class Person:
    def __init__(self, name):
        self.name = name

person = Person('Peter')
print(hasattr(person, 'name')) # True
print(hasattr(person, 'age'))  # False


#__getattr__

class Person:
    def __init__(self, name):
        self.name = name

person = Person('Peter')
print(getattr(person, 'name'))         # True
print(getattr(person, 'age'))          # AttributeError
print(getattr(person, 'age', 'None'))  # None
