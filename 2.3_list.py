# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

user_month = int(input('Введите номер месяца (целое число от 1 до 12):'))

if user_month in winter:
    print('Это зимний месяц.')
elif user_month in spring:
    print('Это весенний месяц.')
elif user_month in summer:
    print('Это летний месяц.')
elif user_month in autumn:
    print('Это осенний месяц.')
else:
    print('Введите корректное значение месяца!')
