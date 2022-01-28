from python_oop_exams.project_20DEC2021.supply import Supply


class Food(Supply):

    def __init__(self, name, energy=25):
        super().__init__(name, energy)
