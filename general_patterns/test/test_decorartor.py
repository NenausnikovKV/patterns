"""Тестирование кофейни, реализованно по паттерну декоратор"""
from general_patterns.coffee_house_decorator.beverage_condiment import Mocha, Whip, Soy
from general_patterns.coffee_house_decorator.coffee import Espresso, DarkRoast, HouseBlend


def test_clear_class():
    """Тестирование работы класса напитка"""
    # Чистый эспрессо
    espresso = Espresso()
    print()
    print(espresso.get_description())
    print(espresso.cost())
    assert espresso.cost() == 1

def test_decorator():
    """Чёрный кофе с двойным шоколадом и взбитыми сливками"""
    dark_roast = DarkRoast()
    mocha_dark_roast = Mocha(dark_roast)
    double_mocha_dark_roast = Mocha(mocha_dark_roast)
    double_mocha_dark_roast_with_whip = Whip(double_mocha_dark_roast)
    print()
    print(double_mocha_dark_roast_with_whip.get_description())
    print(double_mocha_dark_roast_with_whip.cost())
    assert double_mocha_dark_roast_with_whip.cost() == 3.5

def test_consequence_decorator():
    """
    Домашний кофе на соевом молоке с шоколадом и взбитыми сливками
    Запись в одну линию аналог следующего кода
    house_blend = HouseBlend()
    mocha_house_blend = Mocha(house_blend)
    mocha_house_blend_with_soy_milk = Soy(mocha_house_blend)
    mocha_house_blend_with_soy_milk_whip = Whip(mocha_house_blend_with_soy_milk)
    print(mocha_house_blend_with_soy_milk_whip.cost())
    """
    beverage = Whip(Soy(Mocha(HouseBlend())))
    print()
    print(beverage.get_description())
    print(beverage.cost())
    assert beverage.cost() == 2.6
