

from python_polymorphism_and_abstraction.project_wild_farm.animals.animal import Mammal
from python_polymorphism_and_abstraction.project_wild_farm import Vegetable, Fruit, Meat


class Mouse(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        if type(food) != Vegetable and type(food) != Fruit:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.gain_weight(0.10, food)

class Dog(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Woof!'

    def feed(self, food):
        if type(food) != Meat:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.gain_weight(0.4, food)

class Cat(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'Meow'

    def feed(self, food):
        if type(food) != Vegetable and type(food) != Meat:
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.gain_weight(0.3, food)

class Tiger(Mammal):

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return 'ROAR!!!'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
        self.gain_weight(1, food)
