# 4. Дан список, содержащий искажённые данные с должностями и именами сотрудников:
#
# ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки.
# Сформировать и вывести на экран фразы вида: 'Привет, Игорь!'
# Подумать, как получить имена сотрудников из элементов списка, как привести их к корректному виду.
# Можно ли при этом не создавать новый список?

list_employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                  'токарь высшего разряда нИКОЛАй', 'директор аэлита']



for i in range(len(list_employees)):
    employee = list_employees[i].split()
    name = employee[-1]
    print(f'Привет, {name.title()}!')

print('******************************** ')
print('Без создания нового списка: ')
# Тот же результат но без создания нового списка.
# Но если добавить пробел после любого имени работает не корректно, в отличие от первого способа

for i in range(len(list_employees)):
    for m in range(len(list_employees[i]) - 1, -1, -1):
        if list_employees[i][m] == " ":
            print(f'Привет, {list_employees[i][m+1:].title()}!')
            break
