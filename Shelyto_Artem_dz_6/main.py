# list_out = list()
# with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
#     i = 0
#     for line in fr:
#        # list_out.append(get_parse_attrs(line))
#         pars_line = line.split(" ")
#         print(pars_line)
#         # result = (pars_line[0], pars_line[5][1:], pars_line[6])
#         result = (line.split(" ")[0], line.split(" ")[5][1:], line.split(" ")[6])
#         i += 1
#         print(result, type(result), i)
#
#
#
#
# # print(list_out)
# c = ["2", "10"]
# a = "2"
# b = "10"
# print(int(c[0])*int(c[1]))


# import sys
# # интервал для вывода записей
# interval = sys.argv[1:]
# if len(sys.argv) == 1:
#     with open('bakery.csv', 'r', encoding='utf-8') as f:
#         for line in f:
#             print(line.strip())
# # печать строк из файла, если введено одно число (от него и далее по списку)
# elif len(sys.argv) == 2:
#     count = 0
#     with open('bakery.csv', 'r', encoding='utf-8') as f:
#         for line in f:
#             count += 1
#             if int(interval[0]) <= count:
#                 print(line.strip())
# # печать строк из файла, если введен интервал
# elif len(sys.argv) == 3 and int(interval[0]) <= int(interval[1]):
#     count = 0
#     with open('bakery.csv', 'r', encoding='utf-8') as f:
#         for line in f:
#             count += 1
#             if int(interval[0]) <= count <= int(interval[1]):
#                 print(line.strip())
# # если введен интервал не подходящий для работы скрипта
# else:
#     print('интервал для вывода записей введен неверно')
#
# exit()