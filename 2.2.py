# Для списка реализовать обмен значений соседних элементов. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний
# сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию
# input().
list_for_action = []
list_updated = []
list_range = int(input('Введите длинну списка (положительное целое число):'))

for i in range(list_range):
    element_value = input('Введите значение элемента:')
    list_for_action.append(element_value)

for i in range(0, (list_range - 1), 2):
    temp_element = list_for_action[i: i + 2]
    list_updated.append(temp_element[-1])
    list_updated.append(temp_element[0])
if list_range % 2 > 0:
    list_updated.append(list_for_action[-1])

list_for_action = list_updated
print(list_for_action)
