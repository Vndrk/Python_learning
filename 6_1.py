# Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import turtle
import time


class TrafficLight:
    _color = 'grey'

    def switching(self):
        turtle.goto(-20, 60)
        turtle.fillcolor('red')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
        time.sleep(7)
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()

        turtle.circle(30)
        turtle.penup()

        turtle.goto(-20, -10)
        turtle.fillcolor('yellow')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
        time.sleep(2)
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
        turtle.penup()

        turtle.goto(-20, -80)
        turtle.fillcolor('green')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()
        time.sleep(10)
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()

    def __init__(self, color=_color):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(0, 100)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.right(90)
        turtle.forward(220)
        turtle.left(90)
        turtle.backward(100)
        turtle.left(90)
        turtle.forward(220)
        turtle.right(90)
        turtle.forward(100)
        turtle.end_fill()
        turtle.penup()
        turtle.backward(20)
        turtle.left(90)
        turtle.backward(40)

        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()

        turtle.backward(70)
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()

        turtle.backward(70)
        turtle.fillcolor('black')
        turtle.begin_fill()
        turtle.circle(30)
        turtle.end_fill()

        turtle.hideturtle()


svetofor = TrafficLight()
svetofor.switching()
