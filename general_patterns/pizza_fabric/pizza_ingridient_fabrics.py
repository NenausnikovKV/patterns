"""Фабрики ингредиентов для разных пиццерий"""

from abc import ABC

from general_patterns.pizza_fabric.pizza_ingredients import ThinCrustDough, MarinaraSauce, ReggianoCheese, Garlic, \
    Onion, Mushroom, RedPepper, SlicedPepperoni, FreshClaims, ThickCrustDough, PlumTomatoSauce, MozzarellaCheese, \
    BlackOlives, Spinach, EggPlant, FrozenClaims


class IngredientFactoryInterface(ABC):
    """Интерфейс фабрики ингредиентов пиццы"""

    def create_dough(self):
        """Тесто"""

    def create_sauce(self):
        """Соус"""

    def create_cheese(self):
        """Сыр"""

    def create_veggies(self):
        """Овощи"""

    def create_pepperoni(self):
        """Пепперони"""

    def create_clam(self):
        """Морепродукты"""


class NYIngredientFactory(IngredientFactoryInterface):
    """Интерфейс фабрики ингредиентов пиццы"""

    def create_dough(self):
        """Тесто"""
        return ThinCrustDough()

    def create_sauce(self):
        """Соус"""
        return MarinaraSauce()

    def create_cheese(self):
        """Сыр"""
        return ReggianoCheese()

    def create_veggies(self):
        """Овощи"""
        veggies = [Garlic(), Onion(), Mushroom(), RedPepper()]
        return veggies

    def create_pepperoni(self):
        """Пепперони"""
        return SlicedPepperoni()

    def create_clam(self):
        """Морепродукты"""
        return FreshClaims()


class ChicagoIngredientFactory(IngredientFactoryInterface):
    """Интерфейс фабрики ингредиентов пиццы"""

    def create_dough(self):
        """Тесто"""
        return ThickCrustDough()

    def create_sauce(self):
        """Соус"""
        return PlumTomatoSauce()

    def create_cheese(self):
        """Сыр"""
        return MozzarellaCheese()

    def create_veggies(self):
        """Овощи"""
        veggies = [BlackOlives(), Spinach(), EggPlant()]
        return veggies

    def create_pepperoni(self):
        """Пепперони"""
        return SlicedPepperoni()

    def create_clam(self):
        """Морепродукты"""
        return FrozenClaims()
