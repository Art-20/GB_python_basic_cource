# Задание 4
# Написать свой модуль utils и копировать в него функцию currency_rates() из предыдущего задания.
#
# Создать в корневой директории урока, рядом с модулем utils скрипт task_4_4.py,
# в котором импортировать модуль utils и выполнить несколько вызовов функции utils.currency_rates().
#
# Убедиться, что ничего лишнего не происходит.
#
# Приложите в конце скрипта task_4_4.py многострочным комментарием результат его запуска с консоли/терминала.


import utils
import sys

for i in range(len(sys.argv)-1):                    #можно вводить список валют, без учета регистра
    valut = sys.argv.pop()                          #принимает список из терминала и возвращает валюту str
    result = utils.currency_rates(valut)            #вызов ф-ии курса валют
    if result is None:                               #если валюта не найдена
        print(f"курс '{valut}' - не найден")
    else:
        print(f"курс {valut.upper()} - {result} рубля")
exit()

# курсы можно передавать по одному или несколько, без учета регистра букв. В кавычках тоже можно:

# PS C:\Users\Artem\PycharmProjects\GB_python_basic_cource\Shelyto_Artem_dz_4> python task_4_4.py EuR, USD, uAH, Yen, noname
# курс 'noname' - не найден
# курс 'Yen' - не найден
# курс UAH - 24.828 рубля
# курс USD - 74.999 рубля
# курс EUR - 81.224 рубля

# PS C:\Users\Artem\PycharmProjects\GB_python_basic_cource\Shelyto_Artem_dz_4> python task_4_4.py EuR
# курс EUR - 81.224 рубля

# PS C:\Users\Artem\PycharmProjects\GB_python_basic_cource\Shelyto_Artem_dz_4> python task_4_4.py noname
# курс 'noname' - не найден

# PS C:\Users\Artem\PycharmProjects\GB_python_basic_cource\Shelyto_Artem_dz_4> python task_4_4.py USD
# курс USD - 74.999 рубля

# PS C:\Users\Artem\PycharmProjects\GB_python_basic_cource\Shelyto_Artem_dz_4> python task_4_4.py "USD", "руб", BYN
# курс BYN - 27.621 рубля
# курс 'руб' - не найден
# курс USD - 74.999 рубля





