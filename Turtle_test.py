from turtle import *
import time
# Описания библиотеки turtle
# Документация к библиотеке turtle   http://docs.python.org/3/library/turtle.html
# Основные команды для управления черепахой http://server.179.ru/tasks/python/2017b1/pgm12.5_Turtle.html

#-------Пераметры
shift=40
mxmaxs=800
mymaxs=800
#-------Инициализация
t = Turtle()
t.reset()
t.screen.setup(mxmaxs, mymaxs)
#-------Сохранение параметров
a=t.position()
xs=t.xcor()
ys=t.ycor()
t.goto(xs, ys)
#-------Надпись по центру квадрата
t.write('Название', False, 'center', ('times new roman', 25, 'bold'))
time.sleep(1)
t.up()
x=(mxmaxs-shift)//2  # половинный размер Х вписанного в окно квадрата
y=(mymaxs-shift)//2  # половинный размер У вписанного в окно квадрата
#-------Рисуем красный квадрат
t.goto(x, y)
t.color('red')
t.down()
t.left(180); t.forward(x*2);
t.left(90);  t.forward(y*2);
t.left(90);  t.forward(x*2);
t.left(90);  t.forward(y*2);
print(a,'  ',xs, ys)
time.sleep(4)
t.screen.mainloop()       # Задержать окно на экране