from python_polymorphism_and_abstraction.project_animals import Animal

class Cat(Animal):

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return 'Meow meow!'