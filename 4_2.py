# Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его
# формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
# Задание немного выполнил по другому: начальный список задаётся рандомно.



from random import randint, randrange

exam_list = []

for i in range(randrange(5, 20)):
    exam_list.append(randint(0, 1000))


final_list = [exam_list[i] for i in range(1, len(exam_list)) if exam_list[i] > exam_list[i - 1]]

print(exam_list)
print(final_list)
