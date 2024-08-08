"""Простая фабрика для определения класса пиццы"""
from general_patterns.pizza_fabric.pizza import VeggiePizza, ClamPizza, PepperoniPizza, CheesePizza
from general_patterns.pizza_fabric.pizza_exception import WrongPizzaType


class SimplePizzaFactory:
    """Простая фабрика для определения класса пиццы"""

    # noinspection PyMethodMayBeStatic
    def create_pizza(self, pizza_type):
        """Определяем класс по строковому типу"""
        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza()
        elif pizza_type == "clam":
            pizza = ClamPizza()
        elif pizza_type == "veggie":
            pizza = VeggiePizza()
        else:
            raise WrongPizzaType(f"Pizza type {pizza_type} does not exists")
        return pizza
