"""
Прохождение книги head first паттерны ООП
Решение базового примера через миксины
"""

from abc import abstractmethod


class FlyingMixin:
    """
    Миксина. Летать
    Считаем, что все утки летают одинаково
    """
    # noinspection PyMethodMayBeStatic
    def fly(self):
        """ Fly """
        print("Летает")


class BaseQuackingMixin:
    """
    Миксина. Крякать
    Базовое крякание для уток
    В случае, если необходимо другое кряканье можно создать одноименный метод или новую миксину
    """

    # noinspection PyMethodMayBeStatic
    def quack(self):
        """ Say quack """
        print("Крякает")


class Duck:
    """
    Бызовый класс для определиня уток
    """

    def __init__(self):
        pass

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


class MallardDuck(Duck, FlyingMixin, BaseQuackingMixin):
    """ Утка кряква """

    def display(self):
        """ Показываем """
        print("Утка кряква")


class RedheadDuck(Duck, FlyingMixin, BaseQuackingMixin):
    """Нырок американский красноголовый"""

    def display(self):
        """ Показываем """
        print("Нырок американский красноголовый")


class RubberDuck(Duck):
    """Резиновая утка"""
    def display(self):
        """Показываем"""
        print("Резиновая утка")


redhead_duck = RedheadDuck()
redhead_duck.display()
redhead_duck.quack()
redhead_duck.swim()
redhead_duck.fly()
