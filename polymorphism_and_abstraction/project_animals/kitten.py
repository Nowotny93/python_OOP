from python_polymorphism_and_abstraction.project_animals.cat import Cat


class Kitten(Cat):

    GENDER = 'Female'

    def __init__(self, name, age):
        super().__init__(name, age, Kitten.GENDER)

    def make_sound(self):
        return 'Meow'