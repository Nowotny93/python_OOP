from project_10_APR_2021.aquarium.base_aquarium import BaseAquarium

class FreshwaterAquarium(BaseAquarium):
    water = 'Fresh'

    def __init__(self, name):
        super().__init__(name, 50)
