# Задание 1
#
# Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
#
# Например:
#
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
#
# Если перевод сделать невозможно, вернуть None.
#
# Подумайте, как и где лучше хранить информацию, необходимую для перевода:
# какой тип данных выбрать, в теле функции или снаружи.


# 1 вариант  - функция включает словарь. Аргумент только искомое слово. Ввод слов без учета регистра
def num_translate(value: str) -> str:
    """переводит числительное с 1 до 10 с английского на русский
       ,без учета регистра
    """
    en_ru_vocabulary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                       'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    str_out = en_ru_vocabulary.get(value.lower())
    return str_out

print(num_translate("One"))
print(num_translate("eiGhT"))

# 2 вариант  - функция только переводит, словарь можно передать любой в функию. Вввод слов без учета регистра
def translater_num(vacab: dict, value: str) -> str:
    """переводит числительное, словарь загружается в функцию """
    str_out = vacab.get(value.lower())
    return str_out


ru_en_vocabulary = {'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four', 'пять': 'five',
                    'шесть': 'six', 'семь': 'seven', 'восемь': 'eight', 'девять': 'nine', 'десять': 'ten'}
en_ru_vocabulary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five':  'пять',
                    'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

print(translater_num(en_ru_vocabulary, "One"))
print(translater_num(en_ru_vocabulary, "eiGht"))
print(translater_num(ru_en_vocabulary, "ПятЬ"))