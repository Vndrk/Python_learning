# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.


from sys import argv

name, working_hours, rate, bonus = argv

def calc_salary(working_hours, rate, bonus):
    salary = (int(working_hours) * int(rate)) + int(bonus)
    return salary


print(calc_salary(working_hours, rate, bonus))
