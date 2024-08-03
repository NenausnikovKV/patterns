""" Вспоминаю как работает pytest """
from patterns import duck
from patterns import duck_mixins


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
        rubber_duck.quack()
        rubber_duck.swim()
        rubber_duck.fly()


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

    def test_rubber_duck(self):
        """Тест основного функционала RubberDuck"""
        rubber_duck = duck_mixins.RubberDuck()
        rubber_duck.display()
        rubber_duck.swim()
