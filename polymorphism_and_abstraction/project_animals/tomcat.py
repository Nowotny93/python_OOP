from python_polymorphism_and_abstraction.project_animals.cat import Cat

class Tomcat(Cat):

    GENDER = 'Male'

    def __init__(self, name, age):
        super().__init__(name, age, Tomcat.GENDER)

    def make_sound(self):
        return 'Hiss'