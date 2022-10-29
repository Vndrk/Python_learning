# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

def user_data_collect():
    with open('user_data.txt', 'x', encoding='utf-8') as file:
        while True:
            user_str = input('Enter data (press enter without entering data to quit):')
            if len(user_str) == 0:
                return
            else:
                print(user_str, file=file)








user_data_collect()
