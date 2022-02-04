from python_oop_exams.project_15AUG2021 import BakedFood

class Bread(BakedFood):

    def __init__(self, name, price):
        super().__init__(name, 200, price)
