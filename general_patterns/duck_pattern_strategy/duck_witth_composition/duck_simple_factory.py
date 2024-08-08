"""Простая фабрика для определения типа уток"""
from general_patterns.duck_pattern_strategy.duck_exception import WrongDuckType
from general_patterns.duck_pattern_strategy.duck_witth_composition.duck_mixins_with_interfaces import MuteQuackMixin, \
    FlyNoWay, QuackingMixin, FlyWithWingsMixin
from general_patterns.duck_pattern_strategy.duck_witth_composition.duck_with_composition import MallardDuck, \
    RedheadDuck, RubberDuck


class DuckFactory:
    """
    Определяет какая утка нужна и возвращает экземпляр класса реализации
    Если не одна не подходит, поднимает исключение WrongDuckType
    """
    @staticmethod
    def get_duck(duck_name):
        """Определяем тип утки по имени"""
        if duck_name == "redhead_duck":
            fly_behavior = FlyWithWingsMixin()
            quack_behavior = QuackingMixin()
            return RedheadDuck(fly_behavior, quack_behavior)
        if duck_name == "mallard_duck":
            fly_behavior = FlyWithWingsMixin()
            quack_behavior = QuackingMixin()
            return MallardDuck(fly_behavior, quack_behavior)
        if duck_name == "rubber_duck":
            fly_behavior = FlyNoWay()
            quack_behavior = MuteQuackMixin()
            return RubberDuck(fly_behavior, quack_behavior)
        raise WrongDuckType("Wrong duck type name")
