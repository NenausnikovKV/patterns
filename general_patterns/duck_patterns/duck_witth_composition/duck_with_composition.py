"""
Прохождение книги head first паттерны ООП
Решение базового примера через вынесение функционала в другие классы
"""
from abc import abstractmethod

from general_patterns.duck_patterns.duck_exception import WrongDuckType
from general_patterns.duck_patterns.duck_witth_composition.duck_mixins import FlyWithWingsMixin, QuackingMixin, FlyNoWay, \
    FlyingInterface, QuackingInterface, MuteQuackMixin


class DuckFactory:
    """Определяет какая утка нужна"""
    @staticmethod
    def get_duck(duck_name):
        """Определяем тип утки по имени"""
        if duck_name == "redhead_duck":
            return RedheadDuck(fly_behavior=FlyWithWingsMixin(), quack_behavior=QuackingMixin())
        if duck_name == "mallard_duck":
            return MallardDuck(fly_behavior=FlyWithWingsMixin(), quack_behavior=QuackingMixin())
        if duck_name == "rubber_duck":
            return RubberDuck(fly_behavior=FlyNoWay(), quack_behavior=MuteQuackMixin())
        raise WrongDuckType("Wrong duck type name")


class Duck:
    """
    Базовый класс для определения уток
    """
    # В рамках обучения точечно оставлю подсказки типов для интерфейсов, реализующих часть инварианта.
    fly_behavior: FlyingInterface
    quack_behavior: QuackingInterface

    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        """Выполнить полет классами композиции"""
        self.fly_behavior.fly()

    def perform_quack(self):
        """Выполнить кваканье классами композиции"""
        self.quack_behavior.quack()

    # noinspection PyMethodMayBeStatic
    def swim(self):
        """
        Предполагаем, что метод плавать - это неизменная часть инварианта класса утка.
        Поэтому определяем в родительском классе.
        """
        print("Плавает")

    @abstractmethod
    def display(self):
        """
        Метод показывать - изменяющаяся для каждого из классов реализаций часть инварианта.
        Поэтому оставляем в абстрактном виде.
        """


class MallardDuck(Duck):
    """ Утка кряква """

    def display(self):
        """ Показываем """
        print("Утка кряква")


class RedheadDuck(Duck):
    """Нырок американский красноголовый"""

    def display(self):
        """ Показываем """
        print("Нырок американский красноголовый")


class RubberDuck(Duck):
    """Резиновая утка"""

    def display(self):
        """Показываем"""
        print("Резиновая утка")
