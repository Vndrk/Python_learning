# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

with open(r'5_4.txt', 'r', encoding='utf-8') as file_1, \
        open(r'5_4_rus_nums.txt', 'x', encoding='utf-8') as file_2:
    file_1 = file_1.readlines()
    file_1 = ' '.join(file_1)
    file_1 = file_1.replace('One', 'Один')
    file_1 = file_1.replace('Two', 'Два')
    file_1 = file_1.replace('Three', 'Три')
    file_1 = file_1.replace('Four', 'Четыре')
    file_2.write(file_1)
