"""
Тестирование заказа пиццы
Паттерны фабричный метод и абстрактная фабрика
"""

import pytest

from general_patterns.pizza_fabric.pizza_exception import WrongPizzaType
from general_patterns.pizza_fabric.pizza_fabric import SimplePizzaFactory
from general_patterns.pizza_fabric.pizza_store import OldPizzaStore, NYStylePizzaStore, \
    ChicagoStylePizzaStore


def test_pizza():
    """Тест заказа пиццы"""
    pizza_store = OldPizzaStore(pizza_factory=SimplePizzaFactory())
    pizza_store.order_pizza("cheese")
    pizza_store.order_pizza("pepperoni")
    pizza_store.order_pizza("clam")
    pizza_store.order_pizza("veggie")
    with pytest.raises(WrongPizzaType):
        pizza_store.order_pizza("wrong_type_of_pizza")


def test_ny_pizza():
    """Тест заказа нью-йоркской пиццы"""
    pizza_store = NYStylePizzaStore()
    pizza_store.order_pizza("cheese")
    pizza_store.order_pizza("pepperoni")
    pizza_store.order_pizza("clam")
    pizza_store.order_pizza("veggie")
    with pytest.raises(WrongPizzaType):
        pizza_store.order_pizza("wrong_type_of_pizza")


def test_chicago_pizza():
    """Тест заказа чикагской пиццы"""
    pizza_store = ChicagoStylePizzaStore()
    pizza_store.order_pizza("cheese")
    pizza_store.order_pizza("pepperoni")
    pizza_store.order_pizza("clam")
    pizza_store.order_pizza("veggie")
    with pytest.raises(WrongPizzaType):
        pizza_store.order_pizza("wrong_type_of_pizza")
