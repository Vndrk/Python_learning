# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('введите целое число:'))
biggest_number = 0
while number > 0:
    element_compare = number % 10
    number = number // 10
    if element_compare > biggest_number:
        biggest_number = element_compare

print(f'самое большое число: {biggest_number}')
