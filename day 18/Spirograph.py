import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("purple")
tim.speed(0)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for i in range(36):
    a = random_color()
    tim.pencolor(a)
    tim.circle(30)
    tim.left(10)

t.exitonclick()