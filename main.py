from product_manager import ProductManager
from product import Product
from cart import Cart

manager = ProductManager()
cart = Cart()

manager.add_product(Product("Gaming Laptop", 1200, 3))
manager.add_product(Product("Wireless Mouse", 25, 40))
manager.add_product(Product("Mechanical Keyboard", 60, 15))

cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

print("Korpa:")
cart.display_cart()
print(f"Ukupno za naplatu: ${cart.total_cart_value()}")