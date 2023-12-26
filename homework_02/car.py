"""
создайте класс `Car`, наследник `Vehicle`
"""
from base import Vehicle
from engine import Engine


class Car(Vehicle):
    def __init__ (self, engine):
        self.Engine = engine

     def set_engine(self, my_engine):
         self.engine = my_engine

