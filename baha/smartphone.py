from device import Device

class Smartphone(Device):
    def __init__(self, name, price, stock, warranty, screen_size, battery_life):
        super().__init__(name, price, stock, warranty)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f'Smartphone: {self.name}, Price: {self.price}, Screen Size: {self.screen_size}, Battery Life: {self.battery_life} hours'

    def make_call(self):
        print('Smartphone can make a call')

    def install_app(self):
        print('Install application')