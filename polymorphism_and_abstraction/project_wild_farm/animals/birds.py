from python_polymorphism_and_abstraction.project_wild_farm.animals.animal import Bird
from python_polymorphism_and_abstraction.project_wild_farm import Meat


class Owl(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Hoot Hoot'

    def feed(self, food):
        if type(food) != Meat:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.gain_weight(0.25, food)

class Hen(Bird):

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return 'Cluck'

    def feed(self, food):
        self.gain_weight(0.35, food)

