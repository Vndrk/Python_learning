# Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать
# учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета
# были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open(r'5_6.txt', 'r', encoding='utf-8') as f:
    f = f.readlines()
    my_list = []

    subj_list = []
    hours_list = []
    my_gen = (row for row in f)

    for row in my_gen:
        row = row.replace('(л)', '')
        row = row.replace('(лаб)', '')
        row = row.replace('(пр)', '')
        row = row.replace('-', '')
        row = row.replace(':', '')
        row = row.split()
        my_list.append(row)

    for row in my_list:

        for i in row:

            try:
                i = int(i)

            except ValueError:
                subj_list.append(i)
        row.pop(0)

    for row in my_list:
        c = 0
        for i in row:
            i = int(i)
            c += i
        hours_list.append(c)

    subj_dict = dict(zip(subj_list, hours_list))

    print(subj_dict)
