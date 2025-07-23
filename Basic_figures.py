from turtle import *

t = Turtle()

def romb(side, angle):
    """Функция реализует ромб с одним заданным углом и стороной"""
    for i in range(2):
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(180 - angle)

def regular_polygon(n, side):
    """Функция реализует правильный многогранник с заданным числом сторон и длиной стороны"""
    angle = (n-2)*180/n
    for i in range(n):
        t.forward(side)
        t.left(180 - angle)

def square(side):
    """Функция реализует квадрат с заданной стороной"""
    regular_polygon(4, side)

