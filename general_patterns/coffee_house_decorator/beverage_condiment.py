"""Добавки к напиткам"""
from general_patterns.coffee_house_decorator.beverage import Beverage


class Mocha(Beverage):
    """Шоколад"""
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage
        condiment_name = "Mocha"
        self.description = f"{self.beverage.get_description()} {condiment_name}"

    def cost(self):
        condiment_cost = 0.1
        full_cost = self.beverage.cost() + condiment_cost
        return full_cost


class Soy(Beverage):
    """Соевое молоко"""
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage
        condiment_name = "Soy"
        self.description = f"{self.beverage.get_description()} {condiment_name}"

    def cost(self):
        condiment_cost = 0.2
        full_cost = self.beverage.cost() + condiment_cost
        return full_cost


class Whip(Beverage):
    """Взбитые сливки"""
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage
        condiment_name = "Whip"
        self.description = f"{self.beverage.get_description()} {condiment_name}"


    def cost(self):
        condiment_cost = 0.3
        full_cost = self.beverage.cost() + condiment_cost
        return full_cost
