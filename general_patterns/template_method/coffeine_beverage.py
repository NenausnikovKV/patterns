"""coffeine beverage"""
from abc import ABC, abstractmethod


# noinspection PyMethodMayBeStatic
class CoffeineBeverage(ABC):
    """Coffeine beverage preparing"""

    @abstractmethod
    def prepare(self):
        """prepare beverage"""

    def boil_water(self):
        """boiling water"""
        print("boiling water")

    @abstractmethod
    def brew(self):
        """brew beverage"""

    def pour_in_cup(self):
        """pour in cup"""
        print("pour in cup")

    @abstractmethod
    def add_condiments(self):
        """add condiments to beverage"""


# noinspection PyMethodMayBeStatic
class Coffee(CoffeineBeverage):
    """Coffe preparing"""

    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments():
            self.add_condiments()

    def customer_wants_condiments(self):
        """hook for condiments"""
        return True

    def brew(self):
        """dripping coffe through filter"""
        print("dripping coffe through filter")

    def add_condiments(self):
        """add sugar and milk"""
        print("add sugar and milk")


# noinspection PyMethodMayBeStatic
class Tea(CoffeineBeverage):
    """Tea preparing"""
    def prepare(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def brew(self):
        """steep tea bag"""
        print("steep tea bag")

    def add_condiments(self):
        """add lemon"""
        print("add lemon")
