# 5. Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого):
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
#         Например:
#
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
#
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?


from random import choice, shuffle


def get_jokes(amount: int, flag: bool) -> list:
    """ возвращающую n шуток, сформированных из трех
        слов, взятых из трёх списков (по одному из каждого)
        True/False - опция по формирования шуток без повтора слов
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jok_list = []
    if flag: # шутки без повторений
        for i in range(0, amount):
            shuffle(nouns)                     # перемешивает список
            shuffle(adverbs)                   # перемешивает список
            shuffle(adjectives)                # перемешивает список
            noun = nouns.pop()                 # удаляет последнее значение из списка и присваивает его переменной
            adverb = adverbs.pop()             # удаляет последнее значение из списка и присваивает его переменной
            adjectiv = adjectives.pop()        # удаляет последнее значение из списка и присваивает его переменной
            jok_list.extend([f"{noun} {adverb} {adjectiv}"]) # добавляет шутку в список
        return jok_list
    else:  # шутки в которых могут быть повторы слов
        for noun, adverb, adjectiv in zip(nouns, adverbs, adjectives):                   # соединяет шутки
            jok_list.extend([f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}"]) # случайный выбор слов из списка
        return jok_list[:amount]   # передает нужное кол-во шуток


print(get_jokes(5, True))  # количество генерируемых шуток от 1 до 5,
                           # True - слова в шутках не повторяются
                           # False - слова в шутках могут повторятся