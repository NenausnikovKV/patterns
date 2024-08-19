"""
Bird classes
"""
from abc import ABC


class DuckInterface(ABC):
    """Duck interface"""
    def quack(self):
        """quack"""

    def fly(self):
        """fly"""


class MallardDuck(DuckInterface):
    """Mallard duck"""
    def quack(self):
        """quack"""
        print("quack")

    def fly(self):
        """fly"""
        print("fly")


class TurkeyInterface(ABC):
    """Turkey interface"""
    def goble(self):
        """goble"""

    def fly(self):
        """fly"""


class WildTurkey(TurkeyInterface):
    """Wild turkey"""

    # noinspection PyMethodMayBeStatic
    def gobble(self):
        """goble"""
        print("gobble gobble")

    def fly(self):
        """fly a short distance"""
        print("short distance flying")
