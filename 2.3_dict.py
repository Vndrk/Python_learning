# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

season = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}

user_month = int(input('Введите номер месяца (целое число от 1 до 12):'))

for key, value in season.items():
    for i in value:
        if i == user_month:
            if key == 'winter':
                print('Это зимний месяц.')
            elif key == 'spring':
                print('Это весенний месяц.')
            elif key == 'summer':
                print('Это летний месяц.')
            elif key == 'autumn':
                print('Это осенний месяц.')
