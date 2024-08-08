"""Магазин пиццы"""
from abc import abstractmethod

from general_patterns.pizza_fabric.pizza import NYStyleCheesePizza, NYStylePepperoniPizza, NYStyleClamPizza, \
    NYStyleVeggiePizza, ChicagoStyleCheesePizza, ChicagoStylePepperoniPizza, ChicagoStyleClamPizza, \
    ChicagoStyleVeggiePizza
from general_patterns.pizza_fabric.pizza_exception import WrongPizzaType


class OldPizzaStore:
    """Магазин пиццы"""
    def __init__(self, pizza_factory):
        self.pizza_factory = pizza_factory

    def order_pizza(self, pizza_type):
        """Get pizza instance by pizza type a create pizza"""
        # get pizza instance by pizza type
        pizza = self.pizza_factory.create_pizza(pizza_type)
        # create pizza
        pizza.declare_name()
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class PizzaStore:
    """Магазин пиццы"""
    def order_pizza(self, pizza_type):
        """Get pizza instance by pizza type a create pizza"""
        # get pizza instance by pizza type
        pizza = self._create_pizza(pizza_type)
        # create pizza
        pizza.declare_name()
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def _create_pizza(self, pizza_type):
        """Определяет тип пиццы"""


class NYStylePizzaStore(PizzaStore):
    """Пицца в нью-йоркском стиле"""
    def _create_pizza(self, pizza_type):
        """Определяет тип пиццы"""
        if pizza_type == "cheese":
            pizza = NYStyleCheesePizza()
        elif pizza_type == "pepperoni":
            pizza = NYStylePepperoniPizza()
        elif pizza_type == "clam":
            pizza = NYStyleClamPizza()
        elif pizza_type == "veggie":
            pizza = NYStyleVeggiePizza()
        else:
            raise WrongPizzaType(f"Pizza type {pizza_type} does not exists")
        return pizza


class ChicagoStylePizzaStore(PizzaStore):
    """Пицца в Чикагском стиле"""
    def _create_pizza(self, pizza_type):
        """Определяет тип пиццы"""
        if pizza_type == "cheese":
            pizza = ChicagoStyleCheesePizza()
        elif pizza_type == "pepperoni":
            pizza = ChicagoStylePepperoniPizza()
        elif pizza_type == "clam":
            pizza = ChicagoStyleClamPizza()
        elif pizza_type == "veggie":
            pizza = ChicagoStyleVeggiePizza()
        else:
            raise WrongPizzaType(f"Pizza type {pizza_type} does not exists")
        return pizza
