from project_10_APR_2021.fish.base_fish import BaseFish

class FreshwaterFish(BaseFish):
    water = 'Fresh'

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += 3
