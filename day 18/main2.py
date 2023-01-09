import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape("turtle")
tim.pensize(10)
tim.pen(speed=10)
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

angle = [0, 90, 180, 270]

while True:
    a = random_color()
    tim.pencolor(a)
    tim.right(random.choice(angle))
    tim.fd(10)

screen = Screen()
