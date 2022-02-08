from python_oop_exams.project_15AUG2021 import Astronaut

class Biologist(Astronaut):

    def __init__(self, name):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= 5

