"""
создайте класс `Plane`, наследник `Vehicle`
"""

from base import Vehicle
from exceptions import  CargoOverload


class Plane(Vehicle):
    def __init__(self, cargo=0, max_cargo=1000):
        super().__init__()
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, amount):
        total_cargo = self.cargo + amount
        if total_cargo <= self.max_cargo:
            self.cargo = total_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo
