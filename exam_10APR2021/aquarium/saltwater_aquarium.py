from project_10_APR_2021.aquarium.base_aquarium import BaseAquarium

class SaltwaterAquarium(BaseAquarium):
    water = 'Salty'

    def __init__(self, name):
        super().__init__(name, 25)
