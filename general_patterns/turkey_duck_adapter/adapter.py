"""
Turkey adapter for duck
"""
from general_patterns.turkey_duck_adapter.birds import DuckInterface, WildTurkey


class TurkeyAdapter(DuckInterface):
    """object adapter"""
    def __init__(self, turkey):
        self.turkey = turkey

    def quack(self):
        """turkey gobble instead duck quack"""
        self.turkey.gobble()

    def fly(self):
        """5 short turkey flying instead one duck long flying"""
        for _ in range(5):
            self.turkey.fly()


class TurkeyDuckAdapter(DuckInterface, WildTurkey):
    """class adapter"""
    def quack(self):
        """turkey gobble instead duck quack"""
        WildTurkey.gobble(self)
        super().quack()

    def fly(self):
        """5 short turkey flying instead one duck long flying"""
        for _ in range(5):
            WildTurkey.fly(self)
