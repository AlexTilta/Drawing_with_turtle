from turtle import *

t = Turtle()

def square(side):
    for i in range(4):
        t.forward(side)
        t.left(90)

def romb(side, angle):
    """Функция реализует ромб с одним заданным углом и стороной"""
    for i in range(2):
        t.forward(side)
        t.left(angle)
        t.forward(side)
        t.left(180 - angle)

romb(50, 60)
t.screen.mainloop()
