# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
num_sum = 0
with open(r'numbers.txt', 'x', encoding='utf-8') as f_1:
    nums = input('Введите набор чисел, разделённых пробелом:')
    f_1 = f_1.write(nums)

with open(r'numbers.txt', 'r', encoding='utf-8') as f_2:
    f_2 = f_2.readline()
    my_list = f_2.split()

    num_list = []
    for i in my_list:
        i = float(i)
        num_list.append(i)

    num_sum = sum(num_list)

    print(f'Сумма чисел в файле: {num_sum}')
