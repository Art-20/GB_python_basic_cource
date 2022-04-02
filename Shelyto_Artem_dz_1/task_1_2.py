#2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень
#числа X):
#a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 –
#делится нацело на 7. Внимание: использовать только арифметические операции!
#b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
#списка, сумма цифр которых делится нацело на 7.
#c. * Решить задачу под пунктом b, не создавая новый список

print('************* Task_1_2_a *************')

odd_numbers = []
for number in range(1, 1000, 2):
    odd_numbers.append(number ** 3)
print(odd_numbers)  # проверка возведения в куб

total_sum = 0

for number in odd_numbers:
    sum = 0
    #print('число ' + str(number)) #проверка у какого число из списка суммируется цифры
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    #print('сумма ' + str(sum)) #проверка суммы цифр
    if sum % 7 == 0:
        total_sum = total_sum + sum
print('сумма чисел списка, сумма цифр которых делится нацело на 7: ', total_sum)


print('************* Task_1_2_b *************')
# создание нового списка с увеличение элеменов на 17. Улучшен код +=
odd_numbers = []
for number in range(1, 1000, 2):
    odd_numbers.append(number ** 3 + 17)
print(odd_numbers)

total_sum = 0

for number in odd_numbers:
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    if sum % 7 == 0:
        total_sum += sum
print('сумма чисел списка, сумма цифр которых делится нацело на 7: ', total_sum)



print('************* Task_1_2_c *************')

# создание списка по заданию 2а
odd_numbers = []
for number in range(1, 1000, 2):
    odd_numbers.append(number ** 3)
print(odd_numbers)

total_sum = 0

for number in odd_numbers:
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    if sum % 7 == 0:
        total_sum += sum
print('сумма чисел списка, сумма цифр которых делится нацело на 7: ', total_sum)

# выполнение задания 2с, без создания нового списка к каждому эл-ту добавить 17
total_sum = 0  # обнуление счетчика
for number in odd_numbers:
    number += 17
    sum = 0
    while number > 0:
        sum = sum + number % 10
        number = number // 10
    if sum % 7 == 0:
       total_sum = total_sum + sum
print('сумма чисел списка + 17, сумма цифр которых делится нацело на 7: ', total_sum)