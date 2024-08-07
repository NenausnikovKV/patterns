"""Классы исключения Observer"""


class ObserverException(Exception):
    """Исключение Observer"""


class NoOneNotifyingYet(Exception):
    """Еще не было ни одного уведомления"""
