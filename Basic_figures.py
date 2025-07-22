from turtle import *

t = Turtle()

def square(n):
    for i in range(4):
        t.forward(n)
        t.left(90)
square(50)
t.screen.mainloop()
