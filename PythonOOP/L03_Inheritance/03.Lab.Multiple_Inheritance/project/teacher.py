# from L03_Inheritance.Ex02_Zoo.employee import Employee
# from L03_Inheritance.Ex02_Zoo.person import Person
#
from project.employee import Employee
from project.person import Person

class Teacher(Employee, Person):
    def teach(self):
        return "teaching..."
#
# # TODO TEST
# a = Teacher()
# print(a.teach() + " "  + " " + a.sleep() + " " + " " + a.get_fired())