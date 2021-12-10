from python_inheritance.project_multiple_inheritance.person import Person
from python_inheritance.project_multiple_inheritance.employee import Employee

class Teacher(Person, Employee):

    def teach(self):
        return 'teaching...'