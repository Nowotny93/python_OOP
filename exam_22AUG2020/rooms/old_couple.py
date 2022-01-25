from python_oop_exams.project_22AUG2020.appliances.stove import Stove
from python_oop_exams.project_22AUG2020.appliances.fridge import Fridge
from python_oop_exams.project_22AUG2020.appliances import TV
from python_oop_exams.project_22AUG2020.rooms.room import Room

class OldCouple(Room):

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * 2
        self.calculate_expenses(self.appliances)
