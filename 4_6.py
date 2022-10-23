# Реализовать два небольших скрипта:
# ● итератор, генерирующий целые числа, начиная с указанного;
# ● итератор, повторяющий элементы некоторого списка, определённого заранее.
# © geekbrains.ru 20
# Подсказка: используйте функцию count() и cycle() модуля itertools. Обратите внимание, что
# создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3. При достижении числа 10 —
# завершаем цикл. Вторым пунктом необходимо предусмотреть условие, при котором
# повторение элементов списка прекратится.

from itertools import count
from sys import argv


def num_gen(num_start, num_stop):
    for i in count(num_start):
        if i > num_stop:
            return
        else:
            yield i


name, num_start, num_stop = argv

print(*(num_gen(int(num_start), int(num_stop))))

nums = (num_gen(int(num_start), int(num_stop)))

for i in nums:
    print(i)
