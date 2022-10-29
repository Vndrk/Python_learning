# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

with open(r'5_7.txt', 'r', encoding='utf-8') as file:
    ent_data = file.readlines()
    print(ent_data)
    names_list = []
    ent_list = []
    rev_list = []
    cost_list = []
    ent_dict = {}
    profit_dict = {}
    average_profit_dict = {}

    ent_gen = (item for item in ent_data)

    for row in ent_data:
        row = row.split()
        print(row)
        comp_name = row.pop(0)
        names_list.append(comp_name)
        ent = row.pop(0)
        ent_list.append(ent)
        rev = row.pop(0)
        rev_list.append(rev)
        costs = row.pop(0)
        cost_list.append(costs)

    rev_list = [float(i) for i in rev_list]

    cost_list = [float(i) for i in cost_list]

    profit_list = [k - j for k, j in zip(rev_list, cost_list)]

    profit_dict = dict(zip(names_list, profit_list))
    print(profit_dict)

    positive_res_list = [i for i in profit_list if i > 0]

    print(positive_res_list)

    sum_profit = sum(positive_res_list)

    average_profit = round((sum_profit / len(positive_res_list)), 2)

    average_profit_dict['average_profit'] = average_profit

    firm_data = [profit_dict, average_profit_dict]
    print(firm_data)

    with open('comany_data.json', 'x', encoding='utf-8') as file_j:
        json.dump(firm_data, file_j)
