from abc import ABC, abstractmethod

class Vehile(ABC):

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass

class Car(Vehile):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, drive):
        result = (self.fuel_consumption + 0.9) * drive
        if self.fuel_quantity >= result:
            self.fuel_quantity -= result


    def refuel(self, refuel):
        self.fuel_quantity += refuel


class Truck(Vehile):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, drive):
        result = (self.fuel_consumption + 1.6) * drive
        if self.fuel_quantity >= result:
            self.fuel_quantity -= result

    def refuel(self, refuel):
        self.fuel_quantity += refuel * 0.95

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)