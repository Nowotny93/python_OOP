from python_oop_exams.project_22AUG2020.appliances.laptop import Laptop
from python_oop_exams.project_22AUG2020.appliances.fridge import Fridge
from python_oop_exams.project_22AUG2020.appliances import TV
from python_oop_exams.project_22AUG2020.rooms.room import Room

class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        count = 2 + len(children)
        super().__init__(family_name, salary_one + salary_two, count)
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * count
        self.calculate_expenses(self.appliances, self.children)
