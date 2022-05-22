# Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
# ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
# количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
# {
# 100: 15,
# 1000: 3,
# 10000: 7,
# 100000: 2
# }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# © geekbrains.ru 28
# # Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

def upper_limit_size (path: str):
    """
    Определяет размер файла по указанному пути в байтах. Определяет верхнюю границу размера файла кратную 10
    :param path: путь к файлу
    :return: значение верхней границы размера файла

    """
    size = os.stat(path).st_size
    i = 0
    while size > 0:
        size = size // 10
        i += 1
    upper_limit = 10 ** i
    return upper_limit

root_dir = os.path.abspath('some_data')
files = os.listdir(root_dir)
print(root_dir, f'содержит {len(files)} файлов')

# создание словаря
result = {}
for root, dirs, files in os.walk(root_dir):
   for file in files:
       file_name = os.path.join(root, file)
       key = upper_limit_size(file_name)
       i = result.setdefault(key, 0)
       result[key] = i+1

print(result)