from python_inheritance.project_shop.product import Product

class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name: str):
        for pt in self.products:
            if pt.name == product_name:
                self.products.remove(pt)
                break

    def __repr__(self):
        result = ''
        for product in self.products:
            result += f'{product.name}: {product.quantity}'
            result += '\n'
        return result.strip()
