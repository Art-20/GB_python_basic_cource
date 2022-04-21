# Задание 2
# В корневой директории урока создать task_4_2.py и написать в нём функцию currency_rates(),
# принимающую в качестве аргумента код валюты (например, USD, EUR, SGD, ...) и возвращающую курс этой валюты по отношению к рублю.
#
# Использовать библиотеку requests.
#
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
#
# Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
#
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте:
#
# есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом?
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
#
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.


import requests
from decimal import Decimal, ROUND_HALF_UP


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""

    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    valutes = response.get('Valute')             # находит словарь с валютами
    search_valut = valutes.get(code.upper())     # находит словарь запрашиваемой валютой
    if not search_valut == None:                  # проверка есть ли валюта в списке
        # result_value = search_valut.get('Value')       # находит курс,  float
        # return result_value                            # возвращает курс в типе float
        result_value = Decimal(search_valut.get('Value'))               # находит курс,  преобрзует из float в класс Decimal
        return result_value.quantize(Decimal("1.000"), ROUND_HALF_UP)   #возвращает курс в типе Decimal округление до тысячных
    else:
        return
# для расчетов  для точности целесообразно использовать - тип float,
# для визуального восприятия удобнее смотреть на округленные числа - класс Decimal

print(currency_rates("USD"))
print(currency_rates("noname"))
print(currency_rates("BYN"))
print(currency_rates("eUr"))

