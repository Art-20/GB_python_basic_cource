# Задание 2 *(вместо 1)
# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield

# def odd_nums_2(number: int) -> int:
#     """Генератор, возвращающий по очереди нечетные целые числа от 1 до number (включительно)"""
#
#     for i in range (1, number+1, 2):
#         odd_nums_2_gen =(num for num in range(1, number+1, 2))
#         return next(odd_nums_2_gen)
#
#
# n = 15
# generator = odd_nums_2(n)
# for _ in range(1, n + 1, 2):
#     print(next(generator))
#
# # odd_nums_2_gen =(num for num in range(1, 16, 2))
# # print(*odd_nums_2_gen)