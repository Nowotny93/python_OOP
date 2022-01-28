from python_oop_exams.project_20DEC2021.supply import Supply


class Drink(Supply):

    def __init__(self, name, energy=15):
        super().__init__(name, energy)
