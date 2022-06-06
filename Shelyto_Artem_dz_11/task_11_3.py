# 3. Создать собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
# скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и
# строки. Во время ввода пользователем очередного элемента необходимо реализовать
# проверку типа элемента. Вносить его в список, только если введено число. Класс-исключение
# должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.

class OwnError(Exception):
    def __init__(self, in_list):
        self.in_list = in_list
    @staticmethod
    def is_number(str):
        try:
            float(str)
            return True
        except ValueError:
            return False





number_list = []
inp_txt = input("Введите число: ")
try:
    while inp_txt.lower() != "stop":
        if OwnError.is_number(inp_txt):
            number_list.append(float(inp_txt))
            inp_txt = input("Введите число: ")
        else:
            inp_txt = input("Введено не число!!\nВведите число: ")

finally:
    print(f'СПИСОК ЧИСЕЛ:{number_list}\nПрограмма завершена')





