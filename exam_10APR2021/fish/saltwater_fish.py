from project_10_APR_2021.fish.base_fish import BaseFish

class SaltwaterFish(BaseFish):
    water = 'Salty'

    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)

    def eat(self):
        self.size += 2
