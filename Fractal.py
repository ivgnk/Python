# Fractals in Python. Step-by-step guide
# Основа взята из статьи 10 апреля 2020, 10:33.
# Фракталы на Python. Пошаговое руководство
# https://habr.com/ru/company/piter/blog/496538/

# Описания библиотеки turtle
# Документация к библиотеке turtle   http://docs.python.org/3/library/turtle.html
# Основные команды для управления черепахой http://server.179.ru/tasks/python/2017b1/pgm12.5_Turtle.html

# Изменние цвета текста в окне вывода

import turtle, sys
import time
from matplotlib._color_data import BASE_COLORS
from matplotlib._color_data import XKCD_COLORS

# словарь фракталов
fractal_switcher = {
  1:  ("F--F--F",  {"F":"F+F--F+F"}       ,    4 , 60, 'Снежинка Коха'         ,  200, -250),
  2:  ("F+F+F+F",  {"F":"F-F+F+FFF-F-F+F"},    2 , 90, 'Квадратный остров Коха', -100, -00),
  3:  ("F+F+F+F",  {"F":"FF+F++F+F"}      ,    3 , 90, 'Кристалл'              , -250, 200),
  4:  ("F--F"   ,  {"F":"F-F+F+F-F"}      ,    4 , 90, 'Квадратная снежинка'   , -250, 200),
  5:  ("F-F-F-F" ,  {"F":"F-F+F+F-F"}     ,    4 , 90, 'Фрактал Вичека'        , -250, 200),
  6:  (      "F" ,  {"F":"+F--F+"}        ,   10 , 45 , 'Кривая Леви'          , -250, 200 ),
  7:  (     "YF" ,  {"X":"YF+XF+Y", "Y":"XF-YF-X"} , 1  , 60 , 'Ковер Серпинского'       , -250, 200),
  8:  ("FXF--FF--FF" , {"F":"FF", "X":"--FXF++FXF++FXF--"} , 7 , 60, 'Решетка Серпинского', -250, 200),
  9:  ("F+F+F+F"     , {"F":"FF+F+F+F+FF"}                 , 3 , 90, 'Квадрат'            , -250, 200),
 10:  ("F+F+F+F"     , {"F":"FF+F-F+F+FF"}                 , 3 , 90, 'Плитки'       , -250, 200),
 11:  ("F+F+F+F"      , {"F":"FF+F+F+F+F+F-F"}             , 2  , 90, 'Кольца'      , -250, 200),
 12:  ("F+F+F+F"       , {"F":"F+F-F+F+F"}                 , 3  , 90 , 'Крест-2'    , -250, 200),
 13:  ("F++F++F++F++F", {"F":"F++F++F+++++F-F++F"}         , 1  , 36, 'Pentaplexity', -250, 200),
 14:  ("F+F+F+F"      ,  {"F": "-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"}, 3 , 90 , '32-сегментная кривая', -250, 200),
 15:   ("FX"           ,  {"X": "X+YF++YF-FX--FXFX-YF+", "Y": "-FX+YFYF++YF+FX--FX-Y"}     ,  4 , 60 , 'Кривая Пеано-Госпера', -250, 200),
 16:  ("F+XF+F+XF"    ,  {"X": "XF-F+F-XF+F+XF-F+F-X"} , 4  , 90 , 'Кривая Серпинского' , -250, 200),
 17:  (" -X--X"       ,  {"X":"XFX--XFX"}              , 3  , 45 , 'Анклеты Кришны' , -250, 200),
 18:  ("YF"     ,  {"X": "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-",
                    "Y": "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"}, 2 , 90 , 'Квадратный фрактал Госпера' , -250, 200),
 19: ("LFL-F-LFL" , {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"},  0 ,  90 , 'Кривая Мура'  , -250, 200),
 20:  ("L"      ,  {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"},  8 , 90, 'Кривая Гильберта', -250, 200),
 21:  ("X"      ,  {"X":"XFYFX+F+YFXFY-F-XFYFX", "Y":"YFXFY-F-XFYFX+F+YFXFY"}, 4 , 90, 'Кривая Гильберта-II', -250, 200),
 22:  ("F"      ,  {"F":"F+F-F-F-F+F+F+F-F"},  2 , 90, 'Кривая Пеано' , -250, 200),
 23:  ("F+F+F+F",  {"F":"F+FF++F+F"}      ,    3 , 90, 'Крест'        , -250, 200),
 24:  ("F+F+F",    {"F":"F-F+F"},              2 , 120, 'Треугольник' , -250, 200),
 25:  ("FX"     ,  {"X":"X+YF+", "Y":"-FX-Y"}, 8 , 90 , 'Кривая дракона', -250, 200),
 26:  ("F",        {"F":"F-F+F"}             , 5, 120 , 'Кривая Terdragon',      -250, 200),
 27:  ("FX+FX",    {"X":"X+YF+", "Y":"-FX-Y"}, 6,  90 , 'Двойная кривая дракона', -250, 200),
 28:  ("FX+FX+FX", {"X":"X+YF+", "Y":"-FX-Y"}, 7,  90 , 'Тройная кривая дракона', -250, 200)
}

#  работа с цветами
# список цветов
# ! https://undoshutdown.blogspot.com/search/label/имена
# https://jenyay.net/uploads/Matplotlib/Colors/named_colors.png
# ! https://matplotlib.org/examples/color/named_colors.html
ncolors=len(BASE_COLORS)
keylist=list(BASE_COLORS)
def getmycolor(i):
    ic = i % ncolors
    color = BASE_COLORS[keylist[i]]
    return color

# Объявление функций

def create_l_system(iters, axiom, rules):
    start_string = axiom
    if iters == 0:
        return axiom
    end_string = ""
    for _ in range(iters):
        # print(i)
        end_string = "".join(rules[i] if i in rules else i for i in start_string)
        start_string = end_string
    return end_string

def draw_l_system(t, instructions, angle, distance):
    for cmd in instructions:
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)

# def main(iterations, axiom, rules, angle, length=8, size=2, y_offset=-250,
#         x_offset=200, offset_angle=0, width=950, height=950):
#     inst = create_l_system(iterations, axiom, rules)
#     t = turtle.Turtle()
#     wn = turtle.Screen()
#     wn.setup(width, height)
#     t.up()
#     t.backward(-x_offset)
#     t.left(90)
#     t.backward(-y_offset)
#     t.left(offset_angle)
#     t.down()
#     t.speed(0)
#     t.pensize(size)
#     draw_l_system(t, inst, angle, length)
#     t.hideturtle()
#     wn.exitonclick()

def main2(cur, fractals , length=8, size=2, y_offset=-250,
        x_offset=200, offset_angle=0, width=950, height=950):
    t = turtle.Turtle()
    for i in fractals:
        if i!=cur:
            continue
        t.reset()
        (axiom, rules, iterations, angle, namef, x_offset, y_offset ) = fractals[i]
        print(i,namef)

        inst = create_l_system(iterations, axiom, rules)
        wn = turtle.Screen()
        wn.setup(width, height)

        t.color(getmycolor(cur))
        a=t.position()
        t.up()
        t.goto(0, int(height/2.2) ) #
        t.down()
        t.write(namef, False,'center', ('times new roman',25, 'bold'))
        t.up()
        t.goto(a)

        t.up()
        t.backward(-x_offset)
        t.left(90)
        t.backward(-y_offset)
        t.left(offset_angle)
        t.down()
        t.speed(0)
        t.pensize(size)
        draw_l_system(t, inst, angle, length)
        t.hideturtle()
        time.sleep(5)
    wn.exitonclick()



main2(2, fractal_switcher)