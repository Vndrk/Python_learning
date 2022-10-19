# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.

def user_data(user_name=None, surname=None, year_born=None, user_email=None, phone=None):
    print(
        f'Имя: {user_name.capitalize()}, фамилия: {surname.capitalize()}, год рождения: {year_born}, email: {user_email},'
        f'phone: {phone}')


name = input('Введите имя:')
surname = input('Введите фамилию:')
year_born = input('Введите год рождения:')
user_email = input('Введите email:')
phone = input('Введите телефон:')

user_data(user_name=name, surname=surname, year_born=year_born, user_email=user_email, phone=phone)
