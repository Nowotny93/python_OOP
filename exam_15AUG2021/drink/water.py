from python_oop_exams.project_15AUG2021.drink import Drink

class Water(Drink):

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, 1.50, brand)
