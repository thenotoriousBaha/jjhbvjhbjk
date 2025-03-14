class Device:
    def __init__(self, name, price, stock, warranty):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty = warranty

    def __str__(self):
        return f'Device name: {self.name}, Price: {self.price}, Warranty: {self.warranty}'

    def apply_discount(self, percentage):
        self.price -= self.price * (percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        self.stock -= amount