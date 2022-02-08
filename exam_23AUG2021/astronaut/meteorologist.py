from python_oop_exams.project_15AUG2021 import Astronaut

class Meteorologist(Astronaut):

    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= 15

