# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём
# до двух целочисленных разрядов:
#
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
# Сформировать из обработанного списка строку:
#
# в "05" часов "17" минут температура воздуха была "+05" градусов
# Подумать, какое условие записать, чтобы выявить числа среди элементов списка?
# Как модифицировать это условие для чисел со знаком?
#
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к его реализации позже.
# Главное: дополнить числа до двух разрядов нулём!

# Находим интервал кодов который соответствует цифрам от 0 до 9
# print(ord('0'))   #48 int
# print(ord('9'))   #57 int
#print(ord('А'))   #1040
#print(ord('я'))   #1103



list_objects = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for i in range(len(list_objects) - 1, -1, -1):
    for m in range(len(list_objects[i]) - 1, -1, -1):
        if list_objects[i][m].isdigit() and len(list_objects[i]) < 2:
            new_list.extend(['"', f'0{list_objects[i]}', '"'])
            break
        elif list_objects[i][m].isdigit() and list_objects[i][m - 1].isdigit():
            new_list.extend(['"', f'{list_objects[i]}', '"'])
            break
        elif list_objects[i][m].isdigit() and len(list_objects[i]) < 3:
            new_list.extend(['"', f'{list_objects[i][0]}0{list_objects[i][-1]}', '"'])
            break
        else:
            new_list.append(list_objects[i])
            break

print('Исходный список: ', list_objects)
new_list.reverse()
print('Отформатированный список: ', new_list)
print('Сообщение: ', ' '.join(new_list))

# Исходный список отформатирован так как указано в задании,
# но склеить в сообщение не получилось без пробелов. Нужно подумать как это сделать

# Ниже приведен второй вариант решения, сообщение выводится как в задании,
# но список отформатирован без добавления элементов списка с ковычками '"'
# В принципе используя два решения можно вывести нужный результат из каждого, но это не совсем верно.


print('***************** Второй вариант решения ***************')

list_objects = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []

for i in range(len(list_objects)-1, -1, -1):
    for m in range(len(list_objects[i])-1, -1, -1):
       if  list_objects[i][m].isdigit() and len(list_objects[i]) < 2:
           new_list.append(f'"0{list_objects[i]}"')
           break
       elif list_objects[i][m].isdigit() and list_objects[i][m-1].isdigit():
           new_list.append(f'"{list_objects[i]}"')
           break
       elif list_objects[i][m].isdigit() and len(list_objects[i]) < 3:
           new_list.append(f'"{list_objects[i][0]}0{list_objects[i][-1]}"')
           break
       else:
           new_list.append(list_objects[i])
           break

print('Исходный список: ', list_objects)
new_list.reverse()
print('Отформатированный список: ', new_list) #
print('Сообщение: ', ' '.join(new_list))