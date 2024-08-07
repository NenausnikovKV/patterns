"""
Паттерн наблюдатель на основе станции погоды
"""


class WeatherStation:
    """
    Станция погоды.
    Снимает показания датчиков температуры, влажности и давления.
    """
    def __init__(self):
        self._temperature = 20
        self._humidity = 35
        self._pressure = 101325

    def get_temperature(self):
        """Возвращает текущую температуру в градусах цельсия"""
        return self._temperature

    def get_pressure(self):
        """Возвращает текущее давление в Па"""
        return self._pressure

    def get_humidity(self):
        """Возвращает текущую влажность в процентах"""
        return self._humidity

    def _set_new_measurements(self, temperature, pressure, humidity):
        """Добавляем измерения"""
        self._temperature = temperature
        self._pressure = pressure
        self._humidity = humidity
