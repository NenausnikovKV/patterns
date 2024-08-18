"""
Команды
"""
from abc import ABC, abstractmethod


class CommandInterface(ABC):
    """Интерфейс команды"""
    @abstractmethod
    def execute(self):
        """Выполнить"""

    @abstractmethod
    def undo(self):
        """Отменить"""


class NoCommand(CommandInterface):
    """Отсутствие действия по команде"""

    def execute(self):
        """При выполнении команды не делать"""

    def undo(self):
        """Ничего не отменять"""


class LightOnCommand(CommandInterface):
    """Включение света по команде"""
    def __init__(self, light):
        # объект, который что-то делает по команде
        self.light = light

    def execute(self):
        """Выполнение операции по команде - включить свет"""
        self.light.on()

    def undo(self):
        """Отменить"""
        self.light.off()


class LightOffCommand(CommandInterface):
    """Выключение света по команде"""
    def __init__(self, light):
        # объект, который что-то делает по команде
        self.light = light

    def execute(self):
        """Выполнение операции по команде"""
        self.light.off()

    def undo(self):
        """Отменить"""
        self.light.on()


class GarageDoorOpenCommand(CommandInterface):
    """Открытие дверей гаража по команде"""
    def __init__(self, garage_door):
        # объект, который что-то делает по команде
        self.garage_door = garage_door

    def execute(self):
        """Выполнение операции по команде"""
        self.garage_door.up()

    def undo(self):
        """Отменить"""
        self.garage_door.down()


class GarageDoorCloseCommand(CommandInterface):
    """Открытие дверей гаража по команде"""
    def __init__(self, garage_door):
        # объект, который что-то делает по команде
        self.garage_door = garage_door

    def execute(self):
        """Выполнение операции по команде"""
        self.garage_door.down()

    def undo(self):
        """Отменить"""
        self.garage_door.up()


class StereoOnWithCDCommand(CommandInterface):
    """Запуск стерео с сиди"""
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        """Включение стерео с сиди"""
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(volume_value=11)

    def undo(self):
        """Отменить"""
        self.stereo.off()


class StereoOffCommand(CommandInterface):
    """Выключение стерео"""
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        """Выключение стерео"""
        self.stereo.off()

    def undo(self):
        """Отменить"""
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(volume_value=11)


class FanOnCommand(CommandInterface):
    """Включение вентилятора"""

    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        """Выключение вентилятора"""
        self.fan.on()
        self.fan.medium()

    def undo(self):
        """Отменить"""
        self.fan.off()


class FanOffCommand(CommandInterface):
    """Выключение вентилятора"""
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        """Выключение вентилятора"""
        self.fan.off()

    def undo(self):
        """Отменить"""
        self.fan.on()
        self.fan.medium()
