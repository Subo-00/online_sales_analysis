from product_manager import ProductManager
from product import Product
from cart import Cart

manager = ProductManager()
cart = Cart()

manager.add_product(Product("Laptop", 1000, 5))
manager.add_product(Product("Mouse", 20, 50))
manager.add_product(Product("Keyboard", 50, 20))

cart.add_to_cart(manager.products[0])
cart.add_to_cart(manager.products[1])
cart.add_to_cart(manager.products[2])

print("Korpa:")
cart.display_cart()
print(f"Ukupno za naplatu: ${cart.total_cart_value()}")
print("\nInventar:")
manager.display_products()
print(f"Ukupna vrednost: ${manager.total_value()}")