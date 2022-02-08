class AstronautRepository:

    def __init__(self):
        self.astronauts = []

    def add(self, astronaut):

        self.astronauts.append(astronaut)

    def remove(self, astronaut):

        self.astronauts.remove(astronaut)

    def find_by_name(self, name):

        for a in self.astronauts:
            if a.name == name:
                return a

    def find_astronauts_for_mission(self, count, min_oxygen):

        return sorted([x for x in self.astronauts if x.oxygen > min_oxygen],
                      key=lambda x: x.oxygen, reverse=True)[0:count]
