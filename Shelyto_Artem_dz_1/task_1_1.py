#Реализовать вывод информации о промежутке времени в зависимости от его
#продолжительности duration в секундах:
#a. до минуты: <s> сек;
#b. до часа: <m> мин <s> сек;
#c. до суток: <h> час <m> мин <s> сек;
#d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.

print('************* Task 1_1 *************')

duration = int(input('Введите продолжительность в секундах: '))

while duration < 0:
   duration = int(input('Неверное число. Введите положительное число: '))

#duration = 24*3600+5*3600+5*60+8 #ручной ввод для проверки корректности работы

day = duration // 3600 // 24
hours = (duration - day * 24 * 3600) // 3600
minutes = duration % 3600 // 60
seconds = duration % 3600 % 60

if 0 <= duration < 60:
    print('Продолжительность периода: {} сек'.format(seconds))
elif 60 <= duration < 3600:
    print('Продолжительность периода: {} мин {} сек'.format(minutes, seconds))
elif 3600 <= duration < 3600 * 24:
    print('Продолжительность периода: {} час {} мин {} сек'.format(hours, minutes, seconds))
else:
    print('Продолжительность периода: {} дн {} час {} мин {} сек'.format(day, hours, minutes, seconds))

print('************* end *************')