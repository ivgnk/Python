import turtle           # Подключаем модуль turtle
import time

turtle.reset()          # Очищаем экран, приводим черепашку в начальное положение
time.sleep(2)

turtle.pendown()        # Опускаем перо перо (начало рисования)
time.sleep(2)
turtle.forward(50)      # Проползти 50 пикселей вперед
time.sleep(2)

turtle.left(90)         # Поворот влево на 90 градусов
time.sleep(2)
turtle.forward(50)      # Рисуем вторую сторону квадрата
time.sleep(2)

turtle.left(90)
time.sleep(2)
turtle.forward(50)      # Рисуем третью сторону квадрата
time.sleep(2)

turtle.left(90)
time.sleep(2)
turtle.forward(50)      # Рисуем четвертую сторону квадрата
time.sleep(2)

turtle.penup()          # Поднять перо (закончить рисовать)
time.sleep(2)
turtle.forward(100)     # Отвести черепашку от рисунка в сторону

turtle.mainloop()       # Задержать окно на экране