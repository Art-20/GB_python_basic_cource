import sys

def add_sale (sum: float):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.writelines(sum+'\n')
        f.close()


num_list = sys.argv
for i in range(1, len(num_list)):  # можно вводить список через запятую
    add_sale(str(num_list[i]))
    print(f'сумма {num_list[i]}$ добавлена в файл bakery.csv')

exit()