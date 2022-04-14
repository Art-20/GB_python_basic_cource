# Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными,
# начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
#
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(value: str) -> str:
    """переводит числительное с 1 до 10 с английского на русский
       переводит с учетом заглавной буквы
    """
    en_ru_vocabulary = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять',
                        'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    if value.islower():
        str_out = en_ru_vocabulary.get(value.lower())
        return str_out
    else:
        str_out = en_ru_vocabulary.get(value.lower())
        return str_out.capitalize()



print(num_translate_adv("One"))
print(num_translate_adv("eight"))
