from general_patterns.coffee_house_decorator.beverage import Beverage


class Espresso(Beverage):
    """Напиток эспрессо. Описание и стоимость"""
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self):
        beverage_cost = 1
        return beverage_cost


class HouseBlend(Beverage):
    """Домашний кофе"""
    def __init__(self):
        super().__init__()
        self.description = "House blend coffee"

    def cost(self):
        beverage_cost = 2
        return beverage_cost


class DarkRoast(Beverage):
    """Черный кофе"""
    def __init__(self):
        super().__init__()
        self.description = "Dark roast coffee"

    def cost(self):
        beverage_cost = 3
        return beverage_cost


class Decaf(Beverage):
    """Кофе без кофеина"""
    def __init__(self):
        super().__init__()
        self.description = "Decaf coffee"

    def cost(self):
        beverage_cost = 4
        return beverage_cost
