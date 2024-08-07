"""
Класс Duck и его миксины реализаций
"""


from abc import abstractmethod


class FlyingInterface:
    """Интерфейс полета"""
    @abstractmethod
    def fly(self):
        """Абстрактный метод полета"""


class FlyWithWingsMixin(FlyingInterface):
    """
    Миксина. Летать
    Полет с помощью крыльев.
    """
    # noinspection PyMethodMayBeStatic
    def fly(self):
        """ Fly """
        print("Летает")


class FlyNoWay(FlyingInterface):
    """
    Миксина. Летать
    Без возможности полета.
    """
    # noinspection PyMethodMayBeStatic
    def fly(self):
        """
        Без реализации
        Не летает
        """


class QuackingInterface:
    """Абстрактный метод крякать"""
    @abstractmethod
    def quack(self):
        """ Крякать """


class QuackingMixin(QuackingInterface):
    """
    Миксина. Крякать
    Кряканье уток
    """
    # noinspection PyMethodMayBeStatic
    def quack(self):
        """ Крякать"""
        print("Крякает")


class SqueakMixin(QuackingInterface):
    """
    Миксина. Крякать
    Писк резиновой утки
    """
    # noinspection PyMethodMayBeStatic
    def quack(self):
        """ Крякать"""
        print("Писк резиновой утки")


class MuteQuackMixin(QuackingInterface):
    """
    Миксина. Крякать
    Молчаливые утки
    """
    # noinspection PyMethodMayBeStatic
    def quack(self):
        """ Молчать"""
