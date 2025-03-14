class Cart:
    def __init__(self):
        self.items = []  # List of (device, amount) pairs
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
            print(f"Added {amount} of {device.name} to the cart.")
        else:
            print(f"Not enough stock for {device.name}. Only {device.stock} available.")

    def remove_device(self, device, amount):
        for i, (d, a) in enumerate(self.items):
            if d == device:
                if a >= amount:
                    self.items[i] = (d, a - amount)
                    self.total_price -= d.price * amount
                    d.stock += amount  # Revert stock
                    print(f"Removed {amount} of {device.name} from the cart.")
                    break
                else:
                    print(f"Not enough quantity of {device.name} in the cart to remove.")
                    break

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            for device, amount in self.items:
                print(f"{device.name}, Amount: {amount}")

    def checkout(self):
        if not self.items:
            print("Your cart is empty. No items to checkout.")
            return

        print("\nChecking out the following items:")
        for device, amount in self.items:
            if device.is_available(amount):
                device.reduce_stock(amount)
                print(f"{device.name}: {amount} units")
            else:
                print(f"Not enough stock for {device.name}. Only {device.stock} available.")

        print(f"Total price: {self.total_price}")
        self.items.clear()
        self.total_price = 0