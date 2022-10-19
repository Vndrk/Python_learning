# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def max_sum_of_2(a, b, c):
    num_list = [a, b, c]
    num_list.sort(reverse=True)
    sum = num_list[0] + num_list[1]
    return sum


sum = max_sum_of_2(10, 1, 3)

print(sum)



