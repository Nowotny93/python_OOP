from python_encapsulation.project_restaurant.food import Food

class MainDish(Food):

    def __init__(self, name: str, price: float, grams: float):
        super().__init__(name, price, grams)