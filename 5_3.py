# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open(r'5_3.txt', 'r', encoding='utf-8') as file:
    file = file.readlines()
    empl_gen = (row for row in file)

    key_list = []
    value_list = []
    empl_num = 0
    sumary_sal = 0

    for row in empl_gen:
        row = row.split()
        empl_num += 1
        for i in row:
            try:
                i = float(i)
                value_list.append(i)
            except ValueError:
                key_list.append(i)
    empl_dict = dict(zip(key_list, value_list))

    print('Сотрудники имеющие ЗП меньше 20000:')
    for k, v in empl_dict.items():
        if v < 20000:
            print(k)

    for v in empl_dict.values():
        sumary_sal += float(v)

    sumary_sal = round(sumary_sal, 2)
    avg_sal = sumary_sal / empl_num

    print(f'Средняя велмчина дохода сотрудников: {round(avg_sal, 2)}')
