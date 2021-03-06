class Survivor:

    MAX_VALUE = 100

    def __init__(self, name, age, health=100, needs=100):
        self.name = name
        self.age = age
        self.health = health
        self.needs = needs

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name not valid!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age not valid!")
        self.__age = value

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            raise ValueError("Health not valid!")
        elif value > self.MAX_VALUE:
            value = self.MAX_VALUE
        self.__health = value

    @property
    def needs(self):
        return self.__needs

    @needs.setter
    def needs(self, value):
        if value < 0:
            raise ValueError("Needs not valid!")
        elif value > self.MAX_VALUE:
            value = self.MAX_VALUE
        self.__needs = value

    @property
    def needs_sustenance(self):
        return self.needs < 100

    @property
    def needs_healing(self):
        return self.health < 100
