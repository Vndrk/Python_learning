# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь
# ввёл число 3. Считаем 3 + 33 + 333 = 369
number = input('введите число n:')
element_1 = number
element_2 = number + number
element_3 = number + number + number
sum_elements = int(element_1) + int(element_2) + int(element_3)
print(sum_elements)
