# Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# © geekbrains.ru 19
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    is_police = False

    def __init__(self, s, c, n):
        self.speed = s
        self.color = c
        self.name = n

    def go(self):
        print('Car is on the way.')

    def stop(self):
        self.speed = 0
        print('Car is stopped.')

    def turn(self, direction):
        print(f'Car turned {direction}')

    def show_speed(self):
        print(f'Current car speed  {self.speed} km/h.')


class TownCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)

    def show_speed(self):
        if self.speed <= 60:
            print(f'Current car speed  {self.speed} km/h.')
        else:
            print('Speeding!')


class SportCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)


class WorkCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)

    def show_speed(self):
        if self.speed <= 40:
            print(f'Current car speed  {self.speed} km/h.')
        else:
            print('Speeding!')


class PoliceCar(Car):
    is_police = True

    def __init__(self, s, c, n):
        super().__init__(s, c, n)


town_car = TownCar(60, 'black', 'RAM')
print(town_car.name)
print(town_car.color)
print('Is police car !') if town_car.is_police == True else print('Is not police car!')
print(town_car.speed)
town_car.go()
town_car.turn('left')
town_car.show_speed()
town_car.stop()
town_car.show_speed()

sport_car = SportCar(200, 'red', 'Ferrari')
print(sport_car.name)
print(sport_car.color)
print('Is police car !') if sport_car.is_police == True else print('Is not police car!')
print(sport_car.speed)
sport_car.go()
sport_car.turn('right')
sport_car.show_speed()
sport_car.stop()
sport_car.show_speed()

work_car = WorkCar(100, 'brown', 'MAZ')
print(work_car.name)
print(work_car.color)
print('Is police car !') if work_car.is_police == True else print('Is not police car!')
print(work_car.speed)
work_car.go()
work_car.turn('right')
work_car.show_speed()
work_car.stop()
work_car.show_speed()

cop_car = PoliceCar(120, 'blue', 'Ford')
print(cop_car.name)
print(cop_car.color)
print('Is police car !') if cop_car.is_police == True else print('Is not police car!')
print(cop_car.speed)
cop_car.go()
cop_car.turn('right')
cop_car.show_speed()
cop_car.stop()
cop_car.show_speed()
