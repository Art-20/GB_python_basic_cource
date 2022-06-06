# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Елена', 'Жора', 'jkz']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# print(len(tutors))
# print(len(klasses))
# # klasses[len(klasses):] = klasses[:len(tutors)-len(klasses)]
# for _ in range(len(klasses), len(tutors)):
#     klasses.append(None)
# print(len(tutors), tutors)
# print(len(klasses), klasses)

# from time import perf_counter
#
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# start = perf_counter()
# result = []
# print (type(src), len(src))
# # print (src[2])
# for i in range(len(src)-1):
#     if src[i] < src[i+1]:
#         result.append(src[i+1])
# print(result, type(result), perf_counter()-start)
#
# start = perf_counter()
# result = [src[i+1] for i in range(len(src)-1) if src[i] < src[i+1]]
# print(result, type(result), perf_counter()-start)

# # Множества в Python
# basket = ['apple', 'dell', 'samsung', 'apple', 'huawei', 'asus', 'samsung']
# unique_brands = [el for el in basket if basket.count(el) == 1]
# print(unique_brands)
#
# unique_brands = set(basket)
# print(unique_brands)
#
# unique_brands = set()
# tmp = set()
# for el in basket:
#     if el not in tmp:
#         unique_brands.add(el)
#     else:
#         unique_brands.discard(el)
#     tmp.add(el)
# print(unique_brands)