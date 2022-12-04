# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём
# оргтехники на склад и передачу в определённое подразделение компании. Для хранения
# данных о наименовании и количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.

from abc import ABC, abstractmethod


class Office_equipment(ABC):
    @abstractmethod
    def get_item_info(self):
        pass

    def shipping_item(self, destination):
        pass


class Warehouse:

    def __init__(self, c):
        self.printer = 0
        self.desk_top = 0
        self.shredder = 0
        self.capacity = c

    def get_warehouse_info(self):
        ware_house_items = f'Принтеры:{self.printer} шт,\nКомпьютеры:{self.desk_top} шт, Шредеры:{self.shredder} шт, ' \
                           f'\n Свободный объём склада:{round(self.capacity, 2)} m3 '
        return ware_house_items


class Printer(Office_equipment):

    def __init__(self, height_cm, length_cm, width_cm, type, id, location):
        self.height = float(height_cm)
        self.length = float(length_cm)
        self.width = float(width_cm)
        self.type = type
        self.id = id
        self.location = location
        self.get_volume()

    def get_volume(self):
        self.vol = round(((self.height * self.width * self.length) / 1000000), 2)

    def shipping_item(self, destination):
        if self.location == destination:
            print('Товар уже находится в месте назначения!')
        if self.location != 'My_warehouse':
            self.location = destination
        if destination == 'My_warehouse':
            self.location = 'My_warehouse'
            My_warehouse.capacity = My_warehouse.capacity - self.vol
            My_warehouse.printer += 1


class MFP(Printer):
    def __init__(self, height_cm, length_cm, width_cm, type, id, location, dpi_print, dpi_scan):
        super().__init__(height_cm, length_cm, width_cm, type, id, location)
        self.dpi_scan = dpi_scan
        self.dpi_print = dpi_print

    def get_item_info(self):
        item_info = f'Высота:{self.height} см, \nДлина:{self.length} см, \nШирина:{self.width} см, \nId:{self.id}, ' \
                    f'\nМесто нахождения:{self.location},\nРазрешение печати:{self.dpi_print} dpi,\nРазрешение ' \
                    f'сканирования:{self.dpi_scan} dpi '
        return item_info


class Laser_printer(Printer):
    def __init__(self, height_cm, length_cm, width_cm, type, id, location, dpi_print):
        super().__init__(height_cm, length_cm, width_cm, type, id, location)
        self.dpi_print = dpi_print

    def get_item_info(self):
        item_info = f'Высота:{self.height} см, \nДлина:{self.length} см, \nШирина:{self.width} см, \nId:{self.id}, ' \
                    f'\nМесто нахождения:{self.location},\nТип:{self.type},\nРазрешение печати:{self.dpi_print} dpi '
        return item_info


class Desktop(Office_equipment):
    def __init__(self, height_cm, length_cm, width_cm, id, location, cpu):
        self.height = height_cm
        self.length = length_cm
        self.width = width_cm
        self.id = id
        self.location = location
        self.cpu = cpu
        self.get_volume()

    def get_volume(self):
        self.vol = round(((self.height * self.width * self.length) / 1000000), 2)

    def get_item_info(self):
        item_info = f'Высота:{self.height} см, \nДлина:{self.length} см, \nШирина:{self.width} см, \nId:{self.id}, ' \
                    f'\nМесто нахождения:{self.location},\nПроцессор:{self.cpu} '
        return item_info

    def shipping_item(self, destination):
        if self.location == destination:
            print('Товар уже находится в месте назначения!')
        if self.location != 'My_warehouse':
            self.location = destination
        if destination == 'My_warehouse':
            self.location = 'My_warehouse'
            My_warehouse.capacity = My_warehouse.capacity - self.vol
            My_warehouse.desk_top += 1


class Shredder(Office_equipment):
    def __init__(self, height_cm, length_cm, width_cm, id, basket_value, location):
        self.height = height_cm
        self.length = length_cm
        self.width = width_cm
        self.id = id
        self.basket_value = basket_value
        self.location = location
        self.get_volume()

    def get_volume(self):
        self.vol = round(((self.height * self.width * self.length) / 1000000), 2)

    def shipping_item(self, destination):
        if self.location == destination:
            print('Товар уже находится в месте назначения!')
        if self.location != 'My_warehouse':
            self.location = destination
        if destination == 'My_warehouse':
            self.location = 'My_warehouse'
            My_warehouse.capacity = My_warehouse.capacity - self.vol
            My_warehouse.shredder += 1

    def get_item_info(self):
        item_info = f'Высота:{self.height} см, \nДлина:{self.length} см, \nШирина:{self.width} см, \nId:{self.id}, ' \
                    f'\nМесто нахождения:{self.location},\n Емкость корзины:{self.basket_value} л '
        return item_info


My_warehouse = Warehouse(2000)

HP_laser_Laser_135a = MFP(42.4, 40.6, 25.3, 'laser', '0001', None, '1200x1200', '600x600')
HP_laser_Laser_135a.shipping_item('My_warehouse')

Pantum_P2207 = Laser_printer(33.7, 22.2, 17.8, 'laser', '0002', None, '1200x1200')
Pantum_P2207.shipping_item('Sales_dep')

Jet_Wizard = Desktop(50.5, 40, 30, '0003', None, 'intel i5')
Jet_Wizard.shipping_item('My_warehouse')
MultiGame = Desktop(40.5, 40, 30, '0004', None, 'AMD Ryzen 5')
MultiGame.shipping_item('My_warehouse')

print(HP_laser_Laser_135a.get_item_info())
print(Jet_Wizard.get_item_info())

print(My_warehouse.get_warehouse_info())
