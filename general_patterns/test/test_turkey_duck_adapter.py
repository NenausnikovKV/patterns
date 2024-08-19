"""
Test adapter
"""
from general_patterns.turkey_duck_adapter.adapter import TurkeyAdapter, TurkeyDuckAdapter
from general_patterns.turkey_duck_adapter.birds import WildTurkey


def test_turkey_duck_object_adapter():
    """test object adapter"""
    wild_turkey = WildTurkey()
    turkey_duck_adapter = TurkeyAdapter(wild_turkey)

    turkey_duck_adapter.quack()
    turkey_duck_adapter.fly()


def test_turkey_duck_class_adapter():
    """test class adapter"""
    turkey_duck_adapter = TurkeyDuckAdapter()
    turkey_duck_adapter.quack()
    turkey_duck_adapter.fly()
