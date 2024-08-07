from general_patterns.wealth_station_observer.observer_exception import NoOneNotifyingYet


class ObserverInterface:
    """
    Интерфейс наблюдателя.
    Определяем метод, который выполняется при каждой рассылку точки данных
    """
    def update(self, temperature, humidity, pressure):
        """Выполнить обновление при уведомлении"""


class DisplayInterface:
    """
    Интерфейс вывода дынных
    """
    def display(self):
        """Вывести данные"""


class TemperatureScreen(ObserverInterface, DisplayInterface):
    """
    Экран, показывающий температуру
    """
    def __init__(self):
        self.temperature = None

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature

    def display(self):
        if self.temperature is None:
            raise NoOneNotifyingYet("Еще не было получено ни одно уведомление")
        print(f"температура = {self.temperature}")


class AllMeasurementScreen(ObserverInterface, DisplayInterface):
    """
    Экран, показывающий температуру, влажность и атмосферное давление
    """
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

    def display(self):
        if any([self.temperature is None, self.humidity is None, self.pressure is None]):
            raise NoOneNotifyingYet("Еще не было получено ни одно уведомление")
        print(f"температура = {self.temperature} \n"
              f"влажность = {self.humidity} \n"
              f"атмосферное давление = {self.pressure}"
              )
