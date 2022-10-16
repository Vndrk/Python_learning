# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами, то есть характеристиками товара:название, цена, количество,
# единица измерения. Структуру нужно сформировать программно,
# запросив все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например, название. Тогда значение — список
# значений-характеристик, например, список названий товаров.

goods_list = []
unit_tuple_list = []
data_analizing_dict = {}
processing = True
while processing:
    name = input('введите название товара:')
    price = float(input('введите цену товара:'))
    quantity = int(input('введите количество товара:'))
    unit = input('введите ед. товара:')
    process_inquiry = input('Желаете ввести данные еще об одном товаре? (y/n):')
    if process_inquiry == 'y':
        processing = True
    elif process_inquiry == 'n':
        processing = False
    else:
        print('Неверно введенное значение. Процесс будет остановлен')
        processing = False

    unit_dict = {'название': name, 'цена': price, 'количество': quantity, 'ед.': unit}
    goods_list.append(unit_dict)

for unit in enumerate(goods_list, 1):
    unit_tuple_list.append(unit)

temp_goods_listing = []
for i in zip(*unit_tuple_list):
    temp_goods_listing.append(i)

my_list = []
for i in temp_goods_listing:
    i = list(i)
    my_list.append(i)
del my_list[0]
my_list = my_list[0]

for i in my_list:
    for k, v in i.items():
        if data_analizing_dict.get(k, False) is False:
            data_analizing_dict[k] = [v]
        else:
            data_analizing_dict[k].append(v)
data_analizing_dict['ед.'] = set(data_analizing_dict['ед.'])
data_analizing_dict['ед.'] = list(data_analizing_dict['ед.'])
print(data_analizing_dict)
