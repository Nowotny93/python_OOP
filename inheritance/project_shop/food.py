from python_inheritance.project_shop.product import Product

class Food(Product):

    def __init__(self, name):
        super().__init__(name, 15)
