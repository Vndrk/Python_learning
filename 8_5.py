# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# © geekbrains.ru 17
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, real_part, indeterm_part):
        self.real_part = real_part
        self.indeterminate_part = indeterm_part
    def get_comp_number(self):
        if self.indeterminate_part >= 0:
            return f'{self.real_part}+{self.indeterminate_part}j'
        else:
            return f'{self.real_part}{self.indeterminate_part}j'

    def __add__(self, other):
        real_part_sum = self.real_part + other.real_part
        indeterm_part_sum = self.indeterminate_part + other.indeterminate_part
        if indeterm_part_sum >= 0:
            return f'{real_part_sum}+{indeterm_part_sum}j'
        else:
            return f'{real_part_sum}{indeterm_part_sum}j'

    def __mul__(self, other):
        real_part_mul = (self.real_part * other.real_part) - (self.indeterminate_part * other.indeterminate_part)
        indeterm_part_mul = (self.real_part * other.indeterminate_part) + (self.indeterminate_part * other.real_part)
        if indeterm_part_mul >= 0:
            return f'{real_part_mul}+{indeterm_part_mul}j'
        else:
            return f'{real_part_mul}{indeterm_part_mul}j'




c_num_1 = ComplexNumber(6, 5)
c_num_2 = ComplexNumber(-8, -10)
c_num_3 = c_num_1 + c_num_2
c_num_4 = c_num_1 * c_num_2
print(c_num_1.get_comp_number())
print(c_num_2.get_comp_number())
print(c_num_3)
print(c_num_4)


