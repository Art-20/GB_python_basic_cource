# 2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверить его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

inp_1 = input("Введите делимое: ")
inp_2 = input("Введите деитель: ")
try:
    inp_data_1 = int(inp_1)
    inp_data_2 = int(inp_2)
    if inp_data_2 == 0:
        raise OwnError("Вы ввели ноль. Делить на ноль нельзя")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f'Результат {inp_data_1 / inp_data_2}')


# new_object = OwnError()
# print(new_object)
