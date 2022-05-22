
"""
.utils
~~~~~~~~~~~~~~

Этот модуль предоставляет служебные функции, которые используются в запросах.
Используется только для собственных проектов
"""

import requests
from decimal import Decimal, ROUND_HALF_UP


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    valutes = response.get('Valute')             # находит словарь с валютами
    search_valut = valutes.get(code.upper())     # находит словарь запрашиваемой валютой
    if not search_valut == None:                  # проверка есть ли валюта в списке
        result_value = Decimal(search_valut.get('Value'))               # находит курс,  преобрзует из float в класс Decimal
        return result_value.quantize(Decimal("1.000"), ROUND_HALF_UP)   #возвращает курс в типе Decimal округление до тысячных
    else:
        return
