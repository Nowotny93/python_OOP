class PlanetRepository:

    def __init__(self):
        self.planets = []

    def add(self, planet):

        self.planets.append(planet)

    def remove(self, planet):

        self.planets.remove(planet)

    def find_by_name(self, name):

        for p in self.planets:
            if p.name == name:
                return p
        #return None
