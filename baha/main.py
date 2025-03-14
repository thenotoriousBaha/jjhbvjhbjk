from cart import Cart
from device import Device
from smartphone import Smartphone

if __name__ == "__main__":
    # Create devices
    device = Device('Computer', 540, 20, '2028')
    sm1 = Smartphone('iPhone', 100000, 100, '2030', 15, 100)
    sm2 = Smartphone('Redmi', 25000, 99, '2035', 10, 24)

    # Create cart and add devices
    cart = Cart()
    cart.add_device(sm1, 150)
    cart.add_device(sm2, 10)

    # Print cart items and total price
    cart.print_items()
    print(f"Total Price: {cart.get_total_price()}")

    # Proceed to checkout
    cart.checkout()