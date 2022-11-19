# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.

from abc import ABC, abstractmethod


class ClothesTemplate(ABC):
    @abstractmethod
    def show_total_consumption(self):
        pass


class SuitTemplate(ABC):
    def consumption(self):
        pass


class CoatTemplate(ABC):
    def consumtion(self):
        pass


class Clothes(ClothesTemplate):
    _sum_consumption = 0

    def __init__(self, v):
        self._value = v

    @classmethod
    def show_total_consumption(cls):
        return f'Общий расход ткани: {Clothes._sum_consumption}'


class Suit(SuitTemplate, Clothes):
    def __init__(self, v):
        super(SuitTemplate, self).__init__(v)
        self.size = v
        Clothes._sum_consumption += (self._size / 6.5 + 0.5)
        Clothes._sum_consumption = round(Clothes._sum_consumption, 2)

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, v):
        if v < 38:
            self._size = 38
        elif v > 78:
            self._size = 78
        else:
            self._size = v

    def consumption(self):
        c_s = self._size / 6.5 + 0.5

        return round(c_s, 2)


class Coat(CoatTemplate, Clothes):
    def __init__(self, v):
        super(CoatTemplate, self).__init__(v)
        self.height = v
        Clothes._sum_consumption += (2 * self._height + 0.3) / 100
        Clothes._sum_consumption = round(Clothes._sum_consumption, 2)

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, v):
        if v < 100:
            self._height = 100
        elif v > 220:
            self._height = 220
        else:
            self._height = v

    def consumption(self):
        c_c = (2 * self._height + 0.3) / 100

        return round(c_c, 2)


my_suit_1 = Suit(38)
my_suit_2 = Suit(30)
my_suit_3 = Suit(48)
my_suit_4 = Suit(78)
my_suit_5 = Suit(100)

my_coat_1 = Coat(100)
my_coat_2 = Coat(50)
my_coat_3 = Coat(180)
my_coat_4 = Coat(220)
my_coat_5 = Coat(300)

print(my_suit_1.consumption())
print(my_suit_2.consumption())
print(my_suit_3.consumption())
print(my_suit_4.consumption())
print(my_suit_5.consumption())

print(my_coat_1.consumption())
print(my_coat_2.consumption())
print(my_coat_3.consumption())
print(my_coat_4.consumption())
print(my_coat_5.consumption())

print(Clothes.show_total_consumption())
