# Реализовать класс Stationery (канцелярская принадлежность).
# ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит
# сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# ● в каждом классе реализовать переопределение метода draw. Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.

class Statinery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print('Drawing is starting...')


class Pen(Statinery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        super().draw()
        print(f'Drawing by {self.title}')


class Pencil(Statinery):
    def __init__(self, t, c):
        super().__init__(t)
        self.color = c

    def draw(self):
        super().draw()
        print(f'Drawing by {self.title}. Getting such accurate {self.color} lines !!!')


class Handle(Statinery):
    def __init__(self, t):
        super().__init__(t)

    def draw(self):
        super().draw()
        print(f'Drawing by {self.title}. {self.title} is giving us bold lines.')


pen = Pen('Parker')
pen.draw()

pencl = Pencil('Cool pencil', 'red')
pencl.draw()

handle = Handle('Black')
handle.draw()
