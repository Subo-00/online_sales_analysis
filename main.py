from product_manager import ProductManager
from product import Product

manager = ProductManager()
manager.add_product(Product("Laptop", 1000, 5))
manager.add_product(Product("Mouse", 20, 50))
manager.add_product(Product("Keyboard", 50, 20))

manager.display_products()
print(f"Ukupna vrednost: ${manager.total_value()}")