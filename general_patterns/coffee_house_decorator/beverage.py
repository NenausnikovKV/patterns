"""
Напитки и их описания
"""
from abc import abstractmethod


class Beverage:
    """Абстрактный класс напитка"""
    def __init__(self):
        self.description = "Unknown beverage"

    def get_description(self):
        """Возвращает описание напитка"""
        return self.description

    @abstractmethod
    def cost(self):
        """Считает и возвращает стоимость напитка"""


class CondimentBeverageDecorator(Beverage):
    """Декоратор добавок к напитку"""
    @abstractmethod
    def get_description(self):
        """
        Дополняет описание напитка.
        Переопределение метода в классе декораторе.
        """
