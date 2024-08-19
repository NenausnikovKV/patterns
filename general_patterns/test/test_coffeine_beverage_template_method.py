"""test template_method"""
# pylint: disable-next = no-name-in-module
from general_patterns.template_method.coffeine_beverage import Tea, Coffee


def test_coffee():
    """test template_method coffee"""
    coffee = Coffee()
    coffee.prepare()


def test_tea():
    """test template_method tea"""
    tea = Tea()
    tea.prepare()
