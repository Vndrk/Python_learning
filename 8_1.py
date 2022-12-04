# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

class Data:
    date = ''
    day = 0
    month = 0
    year = 0

    def __init__(self, date_str):
        self.date = date_str
        Data.date = self.date
        self.get_date()
        self.date_validation()
        if Data.date == 'Некорректное значение':
            self.date = 'Некорректное значение'
        else:
            pass

    @classmethod
    def get_date(cls):
        date_list = str(cls.date).split('-')
        cls.year = int(date_list.pop())
        cls.month = int(date_list.pop())
        cls.day = int(date_list.pop())

    @staticmethod
    def date_validation():
        if Data.day > 31 or Data.day < 1:
            Data.day = 'Некорректное значение'
        else:
            pass
        if Data.month > 12 or Data.month < 1:
            Data.month = 'Некорректное значение'
        else:
            pass

        if Data.year > 2022 or Data.year < 2000:
            Data.year = 'Некорректное значение'
        else:
            pass

        if Data.day == 'Некорректное значение' or Data.month == 'Некорректное значение' or Data.year == 'Некорректное значение':
            Data.date = 'Некорректное значение'
        else:
            pass




test = Data('31-12-2016')



print(test.day)
print(test.month)
print(test.year)
print(test.date)

test_2 = Data('00-24-3000')

print(test_2.day)
print(test_2.month)
print(test_2.year)
print(test_2.date)



