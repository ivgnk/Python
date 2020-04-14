# 14 января 2019 Графика turtle черепашка в питон
# http://itrobo.ru/programmirovanie/python/grafika-turtle-cherepashka-v-piton.html
# 1 февраля 2019 Примеры графика в python
# http://itrobo.ru/programmirovanie/python/primery-grafika-v-python.html

# goto в Python
# https://tproger.ru/links/python-goto/
# https://stackoverflow.com/questions/438844/is-there-a-label-goto-in-python
# https://github.com/snoack/python-goto

# Метод time.sleep() в Python
# https://programmera.ru/uroki-po-python/metod-time-sleep-v-python/
from turtle import *
import time
import random as r

a = 0
b = 0
col = ["red", "blue", "green", "cyan", "purple"]

def coord():
    global a
    global b
    a = r.randint(-200, 200)
    b = r.randint(-200, 200)

def flower(x, y, color):
    t.up()
    t.goto(x, y - 200)
    t.setheading(90)
    t.color("green")
    t.down()
    t.fd(200)
    t.setheading(0)
    t.color("yellow")
    t.begin_fill()
    t.circle(20, 360)
    t.end_fill()
    for i in range(4):
        t.color(color)
        t.begin_fill()
        t.circle(-35, 360)
        t.end_fill()
        t.color("yellow")
        t.circle(20, 90)
    t.speed(0)
# flower(-250, 250, "red")
# flower(200, -200, "blue")
# flower(100, 100, "green")
# flower(-100, 100, "cyan")
# flower(-200, -200, "purple")

t = Turtle()
t.reset()
t.screen.setup(800, 800)

for i in range(5):
    coord()
    flower(a, b, col[i])

t.screen.exitonclick()

