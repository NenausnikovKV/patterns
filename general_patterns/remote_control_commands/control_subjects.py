"""
Субъекты управления
"""


class Light:
    """Свет в гостиной"""

    # noinspection PyMethodMayBeStatic
    def on(self):
        """Включить свет в гостиной"""
        print("Включить свет в гостиной")

    # noinspection PyMethodMayBeStatic
    def off(self):
        """Выключить свет в гостиной"""
        print("Выключить свет в гостиной")


class GarageDoor:
    """Дверь гаража"""

    # noinspection PyMethodMayBeStatic
    def up(self):
        """open garage door"""
        print("garage door is opened")

    # noinspection PyMethodMayBeStatic
    def down(self):
        """close garage door"""
        print("garage door is closed")

    # noinspection PyMethodMayBeStatic
    def stop(self):
        """stop garage door"""
        print("garage door os stopped")


# noinspection PyMethodMayBeStatic
class Stereo:
    """Управление стерео"""

    def __init__(self):
        self.volume = 5

    def on(self):
        """Включить"""
        print("Включить стерео")

    def off(self):
        """Выключить"""
        print("Выключить стерео")

    def set_cd(self):
        """Выбрать сиди"""
        print("Выбрать сиди стерео")

    def set_dvd(self):
        """Выбрать дивиди"""
        print("Выбрать дивиди стерео")

    def set_radio(self):
        """Выбрать радио"""
        print("Выбрать радио стерео")

    def set_volume(self, volume_value):
        """Установить звук"""
        self.volume = volume_value
        print(f"Установить звук стерео на {volume_value}")


# noinspection PyMethodMayBeStatic
class CeilingFan:
    """Управление потолочным вентилятором"""

    def __init__(self):
        """
        Устанавливаем скорость
        0 -стоит
        1- медленная
        2 - средняя
        3 - быстрая
        """
        self.speed = 0

    def on(self):
        """Включить"""
        print("Включить вентилятор")

    def off(self):
        """Выключить"""
        print("Выключить вентилятор")

    def low(self):
        """Включить медленную скорость"""
        print("Включить медленную скорость")

    def medium(self):
        """Включить среднюю скорость"""
        print("Включить среднюю скорость")

    def high(self):
        """Включить быструю скорость"""
        print("Включить быструю скорость")

    def get_speed(self):
        """Вернуть текущую скорость"""
        return self.speed
