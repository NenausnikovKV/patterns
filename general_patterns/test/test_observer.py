"""
Тестирование паттерна наблюдатель на примере метеостанции
"""
import pytest

from general_patterns.wealth_station_observer.device_sceens import TemperatureScreen, AllMeasurementScreen
from general_patterns.wealth_station_observer.observer_exception import NoOneNotifyingYet
from general_patterns.wealth_station_observer.weather_station_observer import WeatherStationObserverSubject


def test_observer():
    """
    Тест паттерна наблюдатель
    Метеостанция предоставляет данные и уведомляет об изменениях
    """
    # субъект наблюдения - погодная станция
    weather_station = WeatherStationObserverSubject()
    # наблюдатели
    temperature_display = TemperatureScreen()
    all_measurement_display = AllMeasurementScreen()
    # проверяем работу пустых наблюдателей
    with pytest.raises(NoOneNotifyingYet):
        temperature_display.display()
    with pytest.raises(NoOneNotifyingYet):
        all_measurement_display.display()
    # регистрируем наблюдателей
    weather_station.register_observer(temperature_display)
    weather_station.register_observer(all_measurement_display)
    # изменяем данные и передаем уведомление наблюдателям
    weather_station.set_new_measurements_and_notify(1, 1, 1)
    # отображаем данные на экранах
    temperature_display.display()
    all_measurement_display.display()
