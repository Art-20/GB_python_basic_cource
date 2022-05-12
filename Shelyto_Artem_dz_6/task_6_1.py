# Задание 1
# Не используя библиотеки для парсинга,
# распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>) . Например:
#
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]


from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""
    result = (line.split(" ")[0], line.split(" ")[5][1:], line.split(" ")[6])
    return result           # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
       list_out.append(get_parse_attrs(line))

print(list_out, len(list_out))     #печать с кол-ва кортежей в списке (соответсвует кол-ву строк в исходном .txt)