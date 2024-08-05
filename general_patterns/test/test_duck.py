""" Тестирование базового класса утки """
import pytest

from general_patterns.duck_patterns.duck_exception import WrongDuckType
from general_patterns.duck_patterns.duck_witth_composition.duck_with_composition import DuckFactory
from general_patterns.duck_patterns import duck, duck_mixins


class TestDuck:
    """Тест уток, построенных через наследование"""
    def test_mallard_duck(self):
        """Тест основного функционала MallardDuck"""
        mallar_duck = duck.MallardDuck()
        mallar_duck.display()
        mallar_duck.quack()
        mallar_duck.swim()
        mallar_duck.fly()

    def test_redhead_duck(self):
        """Тест основного функционала RedheadDuck"""
        redhead_duck = duck.RedheadDuck()
        redhead_duck.display()
        redhead_duck.quack()
        redhead_duck.swim()
        redhead_duck.fly()

    def test_rubber_duck(self):
        """Тест основного функционала RubberDuck"""
        rubber_duck = duck.RubberDuck()
        rubber_duck.display()
        rubber_duck.swim()


class TestDuckMixin:
    """Тест уток, построенных через наследование и миксины"""
    def test_mallard_duck(self):
        """Тест основного функционала MallardDuck"""
        mallar_duck = duck_mixins.MallardDuck()
        mallar_duck.display()
        mallar_duck.quack()
        mallar_duck.swim()
        mallar_duck.fly()

    def test_redhead_duck(self):
        """Тест основного функционала RedheadDuck"""
        redhead_duck = duck_mixins.RedheadDuck()
        redhead_duck.display()
        redhead_duck.quack()
        redhead_duck.swim()
        redhead_duck.fly()

    def test_rubber_duck_do(self):
        """Тест основного функционала RubberDuck"""
        rubber_duck = duck_mixins.RubberDuck()
        rubber_duck.display()
        rubber_duck.swim()

    # тест методов, которых не должно быть в классе
    # noinspection PyUnresolvedReferences
    def test_rubber_duck_do_not_do(self):
        """Тест, что не должна делать резиновая утка"""
        rubber_duck = duck_mixins.RubberDuck()
        with pytest.raises(AttributeError, match="object has no attribute 'quack'"):
            # pylint: disable-next = no-member
            rubber_duck.quack()
        with pytest.raises(AttributeError, match="object has no attribute 'fly'"):
            # pylint: disable-next = no-member
            rubber_duck.fly()


class TestDuckComposition:
    """Тест уток, построенных через наследование и миксины"""
    def test_mallard_duck(self):
        """Тест основного функционала MallardDuck"""
        mallard_duck = DuckFactory.get_duck("mallard_duck")
        mallard_duck.display()
        mallard_duck.perform_quack()
        mallard_duck.swim()
        mallard_duck.perform_fly()

    def test_redhead_duck(self):
        """Тест основного функционала RedheadDuck"""
        redhead_duck = DuckFactory.get_duck("redhead_duck")
        redhead_duck.display()
        redhead_duck.perform_quack()
        redhead_duck.swim()
        redhead_duck.perform_fly()

    def test_rubber_duck(self):
        """
        Тест основного функционала RubberDuck
        Методы, который не выполняются закрыты заглушкой
        """
        rubber_duck = DuckFactory.get_duck("rubber_duck")
        rubber_duck.display()
        rubber_duck.perform_quack()
        rubber_duck.swim()
        rubber_duck.perform_fly()

    def test_wrong_type_duck(self):
        """
        Тест вызова класса по неверному имени типа уток
        """
        with pytest.raises(WrongDuckType):
            wrong_duck_type = "wrong_duck_type_name"
            DuckFactory.get_duck(wrong_duck_type)
