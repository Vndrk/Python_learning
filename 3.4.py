# Программа принимает действительное положительное число x и целое отрицательное число
# y. Выполните возведение числа x в степень y. Задание реализуйте в виде функции
# my_func(x, y). При решении задания нужно обойтись без встроенной функции возведения
# числа в степень.

def my_func_1(x, y):
    if y > 0:
        y = -y
    z = x ** y
    return z


number = int(input('Введите действительное положительное число:'))
exp_number = int(input('Введите целое отрицательное число:'))

result_1 = my_func_1(number, exp_number)

print(f'Результат вычисления с помощью функции my_func_1: {result_1}')


def my_func_2(x, y):
    z = 1
    if y > 0:
        y = -y
    for i in range(abs(y)):
        z *= x
    return 1 / z


result_2 = my_func_2(number, exp_number)

print(f'Результат вычисления с помощью функции my_func_2: {result_2}')
