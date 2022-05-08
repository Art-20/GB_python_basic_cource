import sys
# интервал для вывода записей
interval = sys.argv[1:]
if len(sys.argv) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())
# печать строк из файла, если введено одно число (от него и далее по списку)
elif len(sys.argv) == 2:
    count = 0
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
            if int(interval[0]) <= count:
                print(line.strip())
# печать строк из файла, если введен интервал
elif len(sys.argv) == 3 and int(interval[0]) <= int(interval[1]):
    count = 0
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            count += 1
            if int(interval[0]) <= count <= int(interval[1]):
                print(line.strip())
# если введен интервал не подходящий для работы скрипта
else:
    print('интервал для вывода записей введен неверно')

exit()