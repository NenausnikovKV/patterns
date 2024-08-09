"""Различная пицца"""
from abc import abstractmethod


class PizzaInterface:
    """Интерфейс приготовления пиццы"""

    @abstractmethod
    def prepare(self):
        """Составить"""

    def bake(self):
        """Выпечь"""

    def cut(self):
        """Нарезать"""

    def box(self):
        """упаковать"""


class Pizza:
    """Интерфейс приготовления пиццы"""

    @abstractmethod
    def __init__(self):
        self.name = "Пицца"
        self.dough = None
        self.sauce = None
        self.veggies = []
        self.cheese = None
        self.pepperoni = None
        self.clam = None

    def declare_name(self):
        """Объявить название пиццы"""
        print(self.name)

    # noinspection PyMethodMayBeStatic
    @abstractmethod
    def prepare(self):
        """Составить"""

    # noinspection PyMethodMayBeStatic
    def bake(self):
        """Выпечь"""
        print("Выпекли")

    # noinspection PyMethodMayBeStatic
    def cut(self):
        """Нарезать"""
        print("Нарезали")

    # noinspection PyMethodMayBeStatic
    def box(self):
        """упаковать"""
        print("Упаковали")


class CheesePizza(Pizza):
    """Сырная пицца"""
    def __init__(self, ingredient_factory):
        self.name = "Сырная пицца"
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class PepperoniPizza(Pizza):
    """Пицца с пепперони"""
    def __init__(self, ingredient_factory):
        self.name = "Пицца с пепперони"
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_pepperoni()


class ClamPizza(Pizza):
    """Пицца с морепродуктами"""
    def __init__(self, ingredient_factory):
        self.name = "Пицца с морепродуктами"
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class VeggiePizza(Pizza):
    """Вегетарианская пицца"""
    def __init__(self, ingredient_factory):
        self.name = "Вегетарианская пицца"
        self.ingredient_factory = ingredient_factory

    def prepare(self):
        print(f"preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_veggies()



# class NYStyleCheesePizza(Pizza):
#     """Нью-Йоркская сырная пицца"""
#     def __init__(self):
#         self.name = "Нью-Йоркская сырная пицца"
#
#
# class NYStylePepperoniPizza(Pizza):
#     """Нью-Йоркская пицца с пепперони"""
#     def __init__(self):
#         self.name = "Нью-Йоркская пицца с пепперони"
#
#
# class NYStyleClamPizza(Pizza):
#     """Нью-Йоркская пицца с морепродуктами"""
#     def __init__(self):
#         self.name = "Нью-Йоркская пицца с морепродуктами"
#
#
# class NYStyleVeggiePizza(Pizza):
#     """Нью-Йоркская вегетарианская пицца"""
#     def __init__(self):
#         self.name = "Нью-Йоркская вегетарианская пицца"
#
#
# class ChicagoStyleCheesePizza(Pizza):
#     """Чикагская сырная пицца"""
#     def __init__(self):
#         self.name = "Чикагская сырная пицца"
#
#
# class ChicagoStylePepperoniPizza(Pizza):
#     """Чикагская пицца с пепперони"""
#     def __init__(self):
#         self.name = "Чикагская пицца с пепперони"
#
#
# class ChicagoStyleClamPizza(Pizza):
#     """Чикагская пицца с морепродуктами"""
#     def __init__(self):
#         self.name = "Чикагская пицца с морепродуктами"
#
#
# class ChicagoStyleVeggiePizza(Pizza):
#     """Чикагская вегетарианская пицца"""
#     def __init__(self):
#         self.name = "Чикагская вегетарианская пицца"
