"""
Прохождение книги head first паттерны ООП
Решение базового примера через вынесение функционала в другие классы
"""
from abc import abstractmethod

from general_patterns.duck_pattern_strategy.duck_exception import WrongDuckType
from general_patterns.duck_pattern_strategy.duck_witth_composition import duck_mixins_with_interfaces




class Duck:
    """
    Базовый класс для определения уток
    """
    # В рамках обучения точечно оставлю подсказки типов для интерфейсов, реализующих часть инварианта.
    fly_behavior: duck_mixins_with_interfaces.FlyingInterface
    quack_behavior: duck_mixins_with_interfaces.QuackingInterface

    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def set_fly_behavior(self, new_fly_behavior):
        """
        Устанавливаем новое поведение для полета.
        Позволяет динамически менять поведение у экземпляра класса.
        """
        self.fly_behavior = new_fly_behavior

    def perform_fly(self):
        """Выполнить полет классами композиции"""
        self.fly_behavior.fly()

    def set_quack_behavior(self, new_quack_behavior):
        """
        Устанавливаем новое поведение для кваканья.
        Позволяет динамически менять поведение у экземпляра класса.
        """
        self.quack_behavior = new_quack_behavior

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
