# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

with open(r'5_2.txt', 'r', encoding='utf-8') as file:
    row_numbers = file.readlines()
    row_numbers.pop()

    my_list = (row for row in row_numbers)

    c = 0
    for row in my_list:
        c += 1
        row = row.split()
        row_count = len(row)
        row = ' '.join(row)
        print(f'{row} В строке слов: {row_count}')
    print(f'Количество строк: {c}')
