""" Тестирование базового класса утки """
import pytest

from duck_patterns.duck_witth_composition.duck_mixins_with_interfaces import SqueakMixin
from general_patterns.duck_patterns.duck_exception import WrongDuckType
from general_patterns.duck_patterns.duck_witth_composition.duck_with_composition import DuckFactory, Duck
from general_patterns.duck_patterns import duck, duck_mixins


class TestDuck:
    """Тест уток, построенных через наследование"""
    def test_mallard_duck(self):
        """Тест основного функционала MallardDuck"""
        mallar_duck = duck.MallardDuck()
        print("\n")
        mallar_duck.display()
        mallar_duck.quack()
        mallar_duck.swim()
        mallar_duck.fly()

    def test_redhead_duck(self):
        """Тест основного функционала RedheadDuck"""
        redhead_duck = duck.RedheadDuck()
        print("\n")
        redhead_duck.display()
        redhead_duck.quack()
        redhead_duck.swim()
        redhead_duck.fly()

    def test_rubber_duck(self):
        """Тест основного функционала RubberDuck"""
        rubber_duck = duck.RubberDuck()
        print("\n")
        rubber_duck.display()
        rubber_duck.swim()


class TestDuckMixin:
    """Тест уток, построенных через наследование и миксины"""
    def test_mallard_duck(self):
        """Тест основного функционала MallardDuck"""
        mallar_duck = duck_mixins.MallardDuck()
        print("\n")
        mallar_duck.display()
        mallar_duck.quack()
        mallar_duck.swim()
        mallar_duck.fly()

    def test_redhead_duck(self):
        """Тест основного функционала RedheadDuck"""
        redhead_duck = duck_mixins.RedheadDuck()
        print("\n")
        redhead_duck.display()
        redhead_duck.quack()
        redhead_duck.swim()
        redhead_duck.fly()

    def test_rubber_duck_do(self):
        """Тест основного функционала RubberDuck"""
        rubber_duck = duck_mixins.RubberDuck()
        print("\n")
        rubber_duck.display()
        rubber_duck.swim()

    # тест методов, которых не должно быть в классе
    # noinspection PyUnresolvedReferences
    def test_rubber_duck_do_not_do(self):
        """Тест, что не должна делать резиновая утка"""
        rubber_duck = duck_mixins.RubberDuck()
        print("\n")
        rubber_duck.display()
        # тест - не крякает
        with pytest.raises(AttributeError, match="object has no attribute 'quack'"):
            # pylint: disable-next = no-member
            rubber_duck.quack()
        print("Не крякает")
        with pytest.raises(AttributeError, match="object has no attribute 'fly'"):
            # pylint: disable-next = no-member
            rubber_duck.fly()
        print("Не летает")


class TestDuckComposition:
    """Тест уток, построенных через наследование и миксины"""
    def test_mallard_duck(self):
        """Тест основного функционала MallardDuck"""
        mallard_duck = DuckFactory.get_duck("mallard_duck")
        print("\n")
        mallard_duck.display()
        mallard_duck.perform_quack()
        mallard_duck.swim()
        mallard_duck.perform_fly()

    def test_redhead_duck(self):
        """Тест основного функционала RedheadDuck"""
        redhead_duck = DuckFactory.get_duck("redhead_duck")
        print("\n")
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
        print("\n")
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

    def test_behavior_changes(self):
        """Тест динамически изменяемого поведения"""
        redhead_duck = DuckFactory.get_duck("redhead_duck")
        print("\n")
        redhead_duck.display()
        redhead_duck.perform_quack()
        redhead_duck.set_quack_behavior(SqueakMixin())
        print("Сменили кваканье")
        redhead_duck.perform_quack()
