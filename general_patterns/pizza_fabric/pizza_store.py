"""Магазин пиццы"""
from abc import abstractmethod

from general_patterns.pizza_fabric.pizza import CheesePizza, PepperoniPizza, ClamPizza, VeggiePizza
from general_patterns.pizza_fabric.pizza_exception import WrongPizzaType
from general_patterns.pizza_fabric.pizza_ingridient_fabrics import NYIngredientFactory


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
        pizza_ny_ingredient_factory = NYIngredientFactory()
        if pizza_type == "cheese":
            pizza = CheesePizza(pizza_ny_ingredient_factory)
            pizza.name = "нью-йоркская сырная пицца"
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(pizza_ny_ingredient_factory)
            pizza.name = "нью-йоркская пепперони пицца"
        elif pizza_type == "clam":
            pizza = ClamPizza(pizza_ny_ingredient_factory)
            pizza.name = "нью-йоркская пицца c морепродуктами"
        elif pizza_type == "veggie":
            pizza = VeggiePizza(pizza_ny_ingredient_factory)
            pizza.name = "нью-йоркская вегетарианская пицца"
        else:
            raise WrongPizzaType(f"Pizza type {pizza_type} does not exists")
        return pizza


class ChicagoStylePizzaStore(PizzaStore):
    """Пицца в Чикагском стиле"""
    def _create_pizza(self, pizza_type):
        """Определяет тип пиццы"""
        pizza_ny_ingredient_factory = NYIngredientFactory()
        if pizza_type == "cheese":
            pizza = CheesePizza(pizza_ny_ingredient_factory)
            pizza.name = "чикагская сырная пицца"
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza(pizza_ny_ingredient_factory)
            pizza.name = "чикагская пепперони пицца"
        elif pizza_type == "clam":
            pizza = ClamPizza(pizza_ny_ingredient_factory)
            pizza.name = "чикагская пицца c морепродуктами"
        elif pizza_type == "veggie":
            pizza = VeggiePizza(pizza_ny_ingredient_factory)
            pizza.name = "чикагская вегетарианская пицца"
        else:
            raise WrongPizzaType(f"Pizza type {pizza_type} does not exists")
        return pizza
