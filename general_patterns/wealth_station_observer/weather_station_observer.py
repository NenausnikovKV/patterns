"""
Наблюдатель для станции погоды
"""
from abc import abstractmethod

from general_patterns.wealth_station_observer.device_sceens import ObserverInterface
from general_patterns.wealth_station_observer.observer_exception import ObserverException
from general_patterns.wealth_station_observer.weather_station import WeatherStation


class ObserverSubject:
    """
    Интерфейс регистрация, удаление и уведомление наблюдателей
    Данные берутся из "субъекта"
    """
    def __init__(self):
        self._observers: list[ObserverInterface] = []

    def register_observer(self, new_observer):
        """Регистрирует нового наблюдателя"""
        if new_observer in self._observers:
            raise ObserverException("The observer already exists.")
        self._observers.append(new_observer)

    def remove_observer(self, observer):
        """Удаляем одного из имеющихся наблюдателей"""
        try:
            self._observers.remove(observer)
        except ValueError as exc:
            raise ObserverException("Can not remove the observer. The observer do not register.") from exc

    @abstractmethod
    def _notify_observers(self):
        """Уведомляем "о чем то, что нам надо" всех имеющихся наблюдателей"""


class WeatherStationObserverSubject(WeatherStation, ObserverSubject):
    """
    Точка данных для наблюдателей
    В рамках учебного проекта оставлю это отдельным классом с наследованием от 2-х классов
    В обычном вероятно нужно будет выполнять в месте - дополнять WeatherStation методами из этого для класса
    """
    def __init__(self):
        WeatherStation.__init__(self)
        ObserverSubject.__init__(self)

    def set_new_measurements_and_notify(self, temperature, pressure, humidity):
        """Изменяем данные и уведомляем наблюдателей"""
        self._set_new_measurements(temperature, pressure, humidity)
        self._notify_observers()

    def _notify_observers(self):
        """Уведомляем "о чем то, что нам надо" всех имеющихся наблюдателей"""
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)
