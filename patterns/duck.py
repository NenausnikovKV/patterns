"""
Прохождение книги head first паттерны ООП
Базовый пример проблемы наследования
"""

from abc import abstractmethod


class Duck:
    """
    Бызовый класс для определиня уток
    """
    def __init__(self):
        pass

    # noinspection PyMethodMayBeStatic
    def quack(self):
        """ Say quack """
        print("Крякает")

    # noinspection PyMethodMayBeStatic
    def swim(self):
        """ Swim """
        print("Плавает")

    # noinspection PyMethodMayBeStatic
    def fly(self):
        """ fly """
        print("Летает")

    @abstractmethod
    def display(self):
        """ show """
        pass


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


# Нарушен принцип Лисков: наследник имеет неожиданное поведение - в отличие от родителя не крякает.
# Класс не переопределил метод fly, что ошибочно, т.к. резиновые утки не летают.
class RubberDuck(Duck):
    """Резиновая утка"""
    def quack(self):
        """Не крякать"""
        pass

    def display(self):
        """Показываем"""
        print("Резиновая утка")
