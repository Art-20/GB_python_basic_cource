# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.


class Data:
    # def __init__(self, in_data):
    #     self.in_data = in_data


    @staticmethod
    def date_extraction(param):
        try:
            extracted_list = param.split("-")
            if not len(extracted_list) == 3:
                raise ValueError ("Неверный формат даты. Необходимо в формате DD-MM-YYYY")
            result = []
            for i in extracted_list:
                result.append(int(i))
            return result
        except ValueError as err:
            return err

    @classmethod
    def date_validation(cls, param):
        data_list = Data().date_extraction(param)
        try:
            year = data_list[2]
            if not 1899 < year < 2101:
                raise ValueError ("Неверный формат даты. Год может быть от 1900 до 2100")
            month = data_list[1]
            if not 0 < month < 13:
                raise ValueError ("Неверный формат даты. Месяц может быть от 01 до 12")
            day = data_list[0]
            month_31 = (1, 3, 5, 7, 8, 10, 12)
            month_30 = (4, 6, 9, 11)
            if month == 2 and not 0 < day < 29:   # еще можно добавить проверку високосного года
                raise ValueError ("Неверный формат даты. В феврале 28 или 29 дней")
            if month in month_31 and not 0 < day < 31:
                raise ValueError ("Неверный формат даты. Проверьте день и месяц")
            if month in month_30 and not 0 < day < 30:
                raise ValueError ("Неверный формат даты. Проверьте день и месяц")
        except ValueError as err:
            return err
        return (f'день: {day}, месяц: {month}, год: {year}')

print(Data.date_extraction('10-02-2022'))

data_1 = Data
print(data_1.date_validation('28-01-1900'))
print(Data.date_validation('28-13-1900'))