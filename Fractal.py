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

width=950
height=920

CurrFrc=0    # Если CurrFrc>=1 and CurrFrc<=NumFractals, то визуализирем фрактал с номером CurrFrc
             # В ином случае визуализирем все фракталы
# словарь фракталов
y_videoshift=30   # Для записи видео, где обрезается низ. y_offset описывает сдвиг вверх
time_sleep_before_play= 15 # Задержка в секундах перед началом отображкения. Нужна при записи видео
fractal_switcher = {
     #  axiom,       rules,           iterations, angle, namef,               x_offset, y_offset, length_, size_
  1:  ("F--F--F",  {"F":"F+F--F+F"}       ,    4 , 60, 'Снежинка Коха'           ,  200, -300,           8, 2),
  2:  ("F+F+F+F",  {"F":"F-F+F+FFF-F-F+F"},    2 , 90, 'Квадратный остров Коха'  , -260, -100,          22, 2),
  3:  ("F+F+F+F",  {"F":"FF+F++F+F"}      ,    3 , 90, 'Кристалл'                , -250, -200,          18, 2),
  4:  ("F--F"   ,  {"F":"F-F+F+F-F"}      ,    4 , 90, 'Квадратная снежинка'     , - 20, -290,           8, 2),
  5:  ("F-F-F-F" , {"F":"F-F+F+F-F"}     ,     4 , 90, 'Фрактал Вичека'          ,  300, -350,           8, 2),
  6:  (      "F" ,  {"F":"+F--F+"}        ,   10 , 45 , 'Кривая Леви'            , -130, -200 ,         12, 2),
  7:  (     "YF" ,  {"X":"YF+XF+Y", "Y":"XF-YF-X"} , 6 , 60 , 'Ковер Серпинского', -230, -350 ,         10, 2),
  8:  ("FXF--FF--FF" , {"F":"FF", "X":"--FXF++FXF++FXF--"} , 6 , 60, 'Решетка Серпинского'                                   , 320,  -450 , 6, 2),
  9:  ("F+F+F+F"     , {"F":"FF+F+F+F+FF"}                 , 3 , 90, 'Квадрат'                                               ,-350,  -320 , 25, 2),
 10:  ("F+F+F+F"     , {"F":"FF+F-F+F+FF"}                 , 3 , 90, 'Плитки'                                                ,  80,   200,  28, 2),
 11:  ("F+F+F+F"      , {"F":"FF+F+F+F+F+F-F"}             , 3  , 90, 'Кольца'                                               , -350,   70, 15, 2),
 12:  ("F+F+F+F"       , {"F":"F+F-F+F+F"}                 , 4  , 90 , 'Крест-2'                                             , -200, -220, 18, 2),
 13:  ("F++F++F++F++F", {"F":"F++F++F+++++F-F++F"}         , 3  , 36, 'Pentaplexity'                                         , -250, -200, 22, 2),
 14:  ("F+F+F+F"      ,  {"F": "-F+F-F-F+F+FF-F+F+FF+F-F-FF+FF-FF+F+F-FF-F-F+FF-F-F+F+F-F+"}, 2 , 90 , '32-сегментная кривая', -150, -180, 5, 2),
 15:  ("FX"           ,  {"X": "X+YF++YF-FX--FXFX-YF+", "Y": "-FX+YFYF++YF+FX--FX-Y"}     ,  4 , 60 , 'Кривая Пеано-Госпера' , -300,  100, 11, 2),
 16:  ("F+XF+F+XF"    ,  {"X": "XF-F+F-XF+F+XF-F+F-X"} , 4  , 90 , 'Кривая Серпинского'                                      , -350,  -00, 12, 2),
 17:  (" -X--X"       ,  {"X":"XFX--XFX"}              , 5  , 45 , 'Анклеты Кришны'                                          ,  400,  -20, 18, 2),
 18:  ("YF"     ,  {"X": "XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-",
                    "Y": "+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY"}, 2 , 90 , 'Квадратный фрактал Госпера' , -260, -250, 20, 2),
 19: ("LFL-F-LFL" , {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"},  4 ,  90 , 'Кривая Мура'                        ,  10,  -250, 18, 2),

 20:  ("L"      ,  {"L":"+RF-LFL-FR+", "R":"-LF+RFR+FL-"},  5 , 90, 'Кривая Гильберта'                      , -300, -270, 18, 2),
 21:  ("X"      ,  {"X":"XFYFX+F+YFXFY-F-XFYFX", "Y":"YFXFY-F-XFYFX+F+YFXFY"}, 3 , 90, 'Кривая Гильберта-II', -250, -250, 20, 2),
 22:  ("F"      ,  {"F":"F+F-F-F-F+F+F+F-F"},  3 , 90, 'Кривая Пеано'           ,   0, -330, 25, 2),
 23:  ("F+F+F+F",  {"F":"F+FF++F+F"}      ,    3 , 90, 'Крест'                  , -250, 200, 38, 2),
 24:  ("F+F+F",    {"F":"F-F+F"},              5 , 120, 'Треугольник'           ,  300, 150, 38, 2),
 25:  ("FX"     ,  {"X":"X+YF+", "Y":"-FX-Y"}, 10 , 90 , 'Кривая дракона'       , -250, -100, 19, 2),
 26:  ("F",        {"F":"F-F+F"}             , 6, 120 , 'Кривая Terdragon'      ,    0,  300, 26, 2),
 27:  ("FX+FX",    {"X":"X+YF+", "Y":"-FX-Y"}, 8,  90 , 'Двойная кривая дракона',  150, -150, 22, 2),
 28:  ("FX+FX+FX", {"X":"X+YF+", "Y":"-FX-Y"}, 7,  90 , 'Тройная кривая дракона',  250,    0, 32, 2)
    #  axiom,       rules,           iterations, angle, namef,               x_offset, y_offset, length_, size_
}

NumFractals=len(fractal_switcher)

#  работа с цветами
# список цветов
# ! https://undoshutdown.blogspot.com/search/label/имена
# https://jenyay.net/uploads/Matplotlib/Colors/named_colors.png
# ! https://matplotlib.org/examples/color/named_colors.html

TABLEAU_COLORS2 = {
    'blue'  : '#1f77b4',
    'orange': '#ff7f0e',
    'green' : '#2ca02c',
    'red'   : '#d62728',
    'purple': '#9467bd',
    'brown' : '#8c564b',
    'pink'  : '#e377c2',
    'gray'  : '#7f7f7f',
    'olive' : '#bcbd22',
    'cyan'  : '#17becf',
}

ncolors=len(BASE_COLORS);        ncolors2=len(TABLEAU_COLORS2);
keylist=list(BASE_COLORS);      keylist2=list(TABLEAU_COLORS2);
print(keylist2)
def getmycolor(i):
    ic = i % ncolors
    color = BASE_COLORS[keylist[ic]]
    return color

def getmycolor2(i):
    ic = i % ncolors2
    color = TABLEAU_COLORS2[keylist2[ic]]
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
def splash(t):
    siz=35;
    t.reset()
    time.sleep(time_sleep_before_play)
    t.up()
    t.goto(0, -height//4-150)
    t.down()

    t.color("blue")
    t.begin_fill()
    t.circle(390) # (20, 360)
    t.end_fill()

    t.hideturtle()
    t.pencolor('#FFAF00')

    t.up();   t.goto(0, 90);     t.down();
    t.write('Фракталы - это' , False,'center', ('arial', siz, 'bold')) # times new roman

    t.up();   t.goto(0, 30);     t.down();
    t.write('самоподобные структуры.' , False,'center', ('arial', siz, 'bold')) # times new roman

    t.up();   t.goto(0, -30);      t.down();
    t.write('Фигура имеет ту же форму,' , False,'center', ('arial', siz, 'bold'))

    t.up();   t.goto(0, -90);   t.down();
    t.write('что и одна или более ее частей' , False,'center', ('arial', siz, 'bold'))
    t.up()
    time.sleep(time_sleep_before_play)


def main2(cur, fractals , width, height, offset_angle=0, ):
    t = turtle.Turtle()
    IsOneFrc=((cur>=1) and (cur<=NumFractals))
    if not IsOneFrc:
        splash(t)
    for i in fractals:
        if IsOneFrc:
            if (i!=cur):
                continue
        else:
            cur=i
        t.reset()
        (axiom, rules, iterations, angle, namef, x_offset, y_offset, length_, size_ ) = fractals[i]
        y_offset=y_videoshift+y_offset # Для записи видео, где обрезается низ. y_offset описывает сдвиг вверх
        print(i,namef)

        inst = create_l_system(iterations, axiom, rules)
        wn = turtle.Screen()
        wn.setup(width, height)

        t.color(getmycolor2(cur))
        a=t.position()
        t.up()
        t.goto(0, int(height/2.2) ) #
        t.down()
        t.write(namef+', фрактал '+str(i)+' из '+str(NumFractals) , False,'center', ('times new roman',25, 'bold'))
        t.up()
        t.goto(a)

        t.up()
        t.backward(-x_offset)
        t.left(90)
        t.backward(-y_offset)
        t.left(offset_angle)
        t.down()
        t.speed(0)
        t.pensize(size_)
        draw_l_system(t, inst, angle, length_)
        t.hideturtle()
        time.sleep(5)
    wn.exitonclick()



main2(CurrFrc, fractal_switcher, width, height)