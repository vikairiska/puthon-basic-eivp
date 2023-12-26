from abc import ABC
from exceptions import LowFuelError
from exceptions import NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, started=True, fuel=300, fuel_consumption=0.3):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started==False:
            raise LowFuelError
    def move(self, dstnc):
        if self.started:
            need = dstnc * self.fuel_consumption
            if self.fuel < need:
                raise NotEnoughFuel

