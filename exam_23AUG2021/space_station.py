
from python_oop_exams.project_15AUG2021 import AstronautRepository
from python_oop_exams.project_15AUG2021 import Biologist
from python_oop_exams.project_15AUG2021 import Geodesist
from python_oop_exams.project_15AUG2021 import Meteorologist
from python_oop_exams.project_15AUG2021 import Planet
from python_oop_exams.project_15AUG2021 import PlanetRepository

class SpaceStation:

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type, name):

        valid_types = ['Biologist', 'Geodesist', 'Meteorologist']

        if self.astronaut_repository.find_by_name(name):
            return f'{name} is already added.'

        if astronaut_type == valid_types[0]:
            astro = Biologist(name)
        elif astronaut_type == valid_types[1]:
            astro = Geodesist(name)
        else:
            astro = Meteorologist(name)

        if astronaut_type not in valid_types:
            raise Exception('Astronaut type is not valid!')

        self.astronaut_repository.add(astro)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name, items):

        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name):

        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            return f"Astronaut {name} doesn't exist!"
        else:
            self.astronaut_repository.remove(astronaut)
            return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):

        for a in self.astronaut_repository.astronauts:
            a.increase_oxygen(10)

    def send_on_mission(self, planet_name):

        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception('Invalid planet name!')

        astronauts = self.astronaut_repository.find_astronauts_for_mission(5, 30)

        if len(astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        participated_astronauts = 0

        for astronaut in astronauts:
            if len(planet.items) == 0:
                break
            while astronaut.oxygen > 0 and len(planet.items) > 0:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            participated_astronauts += 1

        if len(planet.items) == 0:
            self.successful_missions += 1
            return f'Planet: {planet_name} was explored. {participated_astronauts} astronauts participated in ' \
                   f'collecting items. '
        else:
            self.failed_missions += 1
            return 'Mission is not completed.'

    def report(self):

        result = f"{self.successful_missions} successful missions!" + '\n'
        result += f"{self.failed_missions} missions were not completed!" + '\n'
        result += "Astronauts' info:" + '\n'
        for a in self.astronaut_repository.astronauts:
            result += str(a) + '\n'

        return result.strip()
