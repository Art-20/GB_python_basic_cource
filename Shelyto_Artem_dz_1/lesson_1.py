num = 181
if not 0 < num // 100 <= 9:
    print('не трехзначное')
else:
    tens = num % 100 // 10
    if tens == 5:
        print('трехзначное с 5 в центре')
    else:
        print('трехзначное без 5 в центре')

print(9 % 7 == 0)

#HW1 Task 1_2

#last_number = odd_numbers[2]
#print(last_number)
#sum=0
#while last_number > 0:
    #sum = sum + last_number % 10
    #last_number = last_number // 10
    #print('число'+ str(last_number))
    #print('сумма'+ str(sum))