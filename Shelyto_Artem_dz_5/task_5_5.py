# Задание 5
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
#
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.



def get_uniq_numbers(src: list):
    """
    Выбирает уникальные элементы списка.
    Формирует из этих элементов список с сохранением порядка их следования в исходном списке
    """
    uniq_numbers = set()                       #множество уникальных значений
    tmp = set()                                #множество повторяющихся знаений - рабочая переменная
    for num in src:                            #цикл находит уникальные значения, записывает во множество - порядок не сохраняется
        if num not in tmp:
            uniq_numbers.add(num)
        else:
            uniq_numbers.discard(num)
        tmp.add(num)

    result = [num for num in src if num in uniq_numbers]   # List Comprehensions - списка из множества с сохраниение исходной последовательности
    return result



src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))