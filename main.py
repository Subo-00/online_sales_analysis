from product_manager import ProductManager
from product import Product

manager = ProductManager()
manager.add_product(Product("Gaming Laptop", 1200, 3))
manager.add_product(Product("Wireless Mouse", 25, 40))
manager.add_product(Product("Mechanical Keyboard", 60, 15))